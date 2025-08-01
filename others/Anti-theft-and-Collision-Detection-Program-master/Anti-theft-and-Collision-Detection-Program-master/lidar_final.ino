    
/* ---------------------------------------------------------------------------------
 ECE 412 and 413
 Winter and Spring 2019
 Team Members: Ahmed Abu Ghalia, Charles Brandon Barber, Phong Nguyen, Emma Smith
 Author: Emma Smith
 Last Updated: April 10, 2019
   ---------------------------------------------------------------------------------
 Description: This script is for the RPLidar A1.
 The screen is only used for debug purposes. 
 The program checks to see if there has been significant movement 
 ---------------------------------------------------------------------------------- */

#include <RPLidar.h>
#include <Wire.h>
#include "SSD1306Ascii.h"
#include "SSD1306AsciiWire.h"


/* Object Instantiation */
RPLidar lidar;
// Global variables
float locations[72]; // Keep track of the last locations for every 5 degrees (this is to optimize memory)
bool cameras_off = true;  // Check before turning cameras off. True to turn off and false to leave on
int loops_elapsed = 0;
bool lastStartBit = true;

/* Pin Definitions */
#define RPLIDAR_MOTOR 3 // The PWM pin for control the speed of RPLIDAR's motor.
                        // This pin should connected with the RPLIDAR's MOTOCTRL signal 
// For the cameras
#define SELECT_LINE 8
#define RELAY_LINE 7

// To communicate with the RPI
#define CAMERAS_BUSY 4 //This will be high when the cameras are available
#define CAMERAS_REQUEST 5 //Set this high then we need the cameras
#define COLLISION_OCURRED 6

/* Program Constants */
#define distance_minumum_change 1000
#define min_record 10000

/* For the screen */
#define I2C_ADDRESS 0x3C
#define RST_PIN -1
SSD1306AsciiWire oled;
                        
void setup() {
  // bind the RPLIDAR driver to the arduino hardware serial
  lidar.begin(Serial);
 
  // set pin modes
  pinMode(RPLIDAR_MOTOR, OUTPUT);
  pinMode(SELECT_LINE, OUTPUT);
  pinMode(RELAY_LINE, OUTPUT);
  pinMode(CAMERAS_BUSY, INPUT);
  pinMode(CAMERAS_REQUEST, OUTPUT);
  pinMode(COLLISION_OCURRED, OUTPUT);

  /* Initialize the wire (to communicate over I2c)*/
  Wire.begin();
  Wire.setClock(400000L);

  // Initialize the screen to the propper address and size
  #if RST_PIN >= 0
    oled.begin(&Adafruit128x64, I2C_ADDRESS, RST_PIN);
  #else // RST_PIN <= 0
    oled.begin(&Adafruit128x64, I2C_ADDRESS);
  #endif // RST_PIN >= 0  

  oled.setFont(Adafruit5x7); 
  oled.clear(); 
  oled.print("the screen is on");
}

// Turn on cameras and start recording
void turn_on_cameras ()
{
  while(digitalRead(CAMERAS_BUSY) == LOW) {
    oled.clear();
    oled.print("Waiting for the camera\nCamera Busy and Cameras Request: ");
    oled.print(digitalRead(CAMERAS_BUSY));
    oled.print(digitalRead(CAMERAS_REQUEST));
    delay(100);
  }
 
  // reset loops
   loops_elapsed = 0;
  // Turn off gpio pin to RPI. this will only be triggered by accelerometer
  // Check to see if the cameras are already on. Don't want to re-short the lines
  if (cameras_off == true) {
    digitalWrite(RELAY_LINE, HIGH);
    digitalWrite(SELECT_LINE, HIGH);
  // Short the data lines to start recording
  // Stop shorting the data lines after a delay (need to find out from Brandon and Ahmed)
    cameras_off = false;
    oled.clear();
    oled.print("Turning cameras on!\nCamera Busy and Cameras Request: ");
    oled.print(digitalRead(CAMERAS_BUSY));
    oled.print(digitalRead(CAMERAS_REQUEST));
  }
  // If the cameras are already on, you should do nothing. 
  else  if (cameras_off == false){
    oled.clear();
    oled.print("Cameras already on!\nCamera Busy and Cameras Request: ");
    oled.print(digitalRead(CAMERAS_BUSY));
    oled.print(digitalRead(CAMERAS_REQUEST));
  }
  else {
    oled.clear();
    oled.print("This should never happen");
  }
}

// Turn off cameras and stop recording as long as collision danger is gone
void turn_off_cameras ()
{
  // Open the relay

  // Switch the select lines
  // Close the relay
  // Let the Rpi know that the Arduino no longer needs the camera
  digitalWrite(CAMERAS_REQUEST, LOW);
  cameras_off = true;

  oled.clear();
  oled.print("Cameras would be off!\nCamera Busy and Cameras Request: ");
  oled.print(digitalRead(CAMERAS_BUSY));
  oled.print(digitalRead(CAMERAS_REQUEST));  
}

void loop() {
  if (IS_OK(lidar.waitPoint())) {
    float distance = lidar.getCurrentPoint().distance; //distance value in mm unit
    float angle    = lidar.getCurrentPoint().angle; //anglue value in degree
    bool  startBit = lidar.getCurrentPoint().startBit; //whether this point is belong to a new scan
    byte  quality  = lidar.getCurrentPoint().quality; //quality of the current measurement

    // If the distance has changed significantly since the last time we checked that angle, then turn on the cameras
   // if ((abs(distance - locations[(int)angle/5]) > distance_minumum_change) && (locations[(int)angle/5] != 0) && (startBit != lastStartBit){
   if (distance > 200 && (startBit != lastStartBit)){
      // send request to RPi for cameras
      digitalWrite(CAMERAS_REQUEST, HIGH);
      turn_on_cameras();
    }
    lastStartBit = startBit;
    locations[(int)angle/5] = distance;    
    
  } else {
    analogWrite(RPLIDAR_MOTOR, 0); //stop the rplidar motor
    
    // try to detect RPLIDAR... 
    rplidar_response_device_info_t info;
    if (IS_OK(lidar.getDeviceInfo(info, 100))) {
       // detected...
       lidar.startScan();       
       // start motor rotating. Max allowed is 255
       analogWrite(RPLIDAR_MOTOR, 150);
       delay(500);
       oled.clear();
       oled.print("Tried detecting lidar");
    }
  }
  // If the cameras have been on for at least 5 minutes and there is no longer any danger
    // turn off the cameras
   ++loops_elapsed;
   if (loops_elapsed >=  min_record && !cameras_off)
    turn_off_cameras();
}
