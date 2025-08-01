#from imutils.video import VideoStream
import cv2
import time
import f_detector
#import imutils
import numpy as np



# iniciar variables para el detector de parapadeo
COUNTER = 0
TOTAL = 0
#video_capture = cv2.VideoCapture(0)
# ----------------------------- video -----------------------------
#ingestar data
#vs = VideoStream(src=0).start()
#while True:
    #im = video_capture.read()
    #ret, frame = video_capture.read()
    #im = cv2.flip(im, 1)
    #im = imutils.resize(im, width=720)
def blink(frame):
    # iniciar variables para el detector de parapadeo
    detector = f_detector.eye_blink_detector()
    COUNTER = 0
    TOTAL = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detectar_rostro    
    rectangles = detector.detector_faces(gray, 0)
    boxes_face = f_detector.convert_rectangles2array(rectangles,frame)
    if len(boxes_face)!=0:
        # seleccionar el rostro con mas area
        areas = f_detector.get_areas(boxes_face)
        index = np.argmax(areas)
        rectangles = rectangles[index]
        boxes_face = np.expand_dims(boxes_face[index],axis=0)
        # blinks_detector
        COUNTER,TOTAL = detector.eye_blink(gray,rectangles,COUNTER,TOTAL)
        # agregar bounding box
        img_post = f_detector.bounding_box(frame,boxes_face,['blinks: {}'.format(TOTAL)])
        return img_post
    else:
        #img_post = frame
        return frame


# cv2.imshow('blink_detection',img_post)
# if cv2.waitKey(1) &0xFF == ord('q'):
#     break