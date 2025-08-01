# On the Raspberry Pi with the USB-to-serial converter:
import serial
uart = serial.Serial("COM8", baudrate=9600, timeout=3000)

import adafruit_thermal_printer
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
p = ThermalPrinter(uart)
#
# p.print('Hello from CircuitPython!')
# p.feed(5)



def printcandidates(pres,vice,sec,trea):
    p.underline = adafruit_thermal_printer.UNDERLINE_THICK
    p.size = adafruit_thermal_printer.SIZE_MEDIUM
    p.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    p.print('CANDIDATES SELECTED')
    p.feed(1)
    p.underline = None
    p.size = adafruit_thermal_printer.SIZE_SMALL
    p.justify = adafruit_thermal_printer.JUSTIFY_LEFT
    p.print('President: '+pres)
    p.print('Vice-President: ' + vice)
    p.print('Secretary: ' + sec)
    p.print('Treasurer: ' + trea)
    p.feed(6)

def totalVotes(pres,vice,sec,trea):
    p.underline = adafruit_thermal_printer.UNDERLINE_THICK
    p.size = adafruit_thermal_printer.SIZE_MEDIUM
    p.justify = adafruit_thermal_printer.JUSTIFY_CENTER
    p.print('Vote Counts')
    p.feed(1)
    p.underline = None
    p.size = adafruit_thermal_printer.SIZE_SMALL
    p.justify = adafruit_thermal_printer.JUSTIFY_LEFT
    p.print('President:')
    for Akey, Aval in pres.items():
        p.print(f"{Akey} = {Aval}")
    p.print('\nVice-President:')
    for Bkey, Bval in vice.items():
        p.print(f"{Bkey} = {Bval}")
    p.print('\nSecretary:')
    for Ckey, Cval in sec.items():
        p.print(f"{Ckey} = {Cval}")
    p.print('\nTreasurer:')
    for Dkey, Dval in trea.items():
        p.print(f"{Dkey} = {Dval}")
    p.feed(4)





