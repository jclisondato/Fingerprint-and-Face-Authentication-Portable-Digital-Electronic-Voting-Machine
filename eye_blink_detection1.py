import cv2
import f_detector
import numpy as np


def call():
    # instancio detector
    detector = f_detector.eye_blink_detector()
    # iniciar variables para el detector de parapadeo
    COUNTER = 0
    TOTAL = 0

    # ----------------------------- video -----------------------------
    #ingestar data
    #vs = VideoStream(src=0).start()
    cap = cv2.VideoCapture(0)
    while True:
        ret, im = cap.read()
        #im = cv2.flip(im, 1)
       # im = imutils.resize(im, width=720)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # detectar_rostro
        rectangles = detector.detector_faces(gray, 0)
        boxes_face = f_detector.convert_rectangles2array(rectangles,im)
        if len(boxes_face)!=0:
            # seleccionar el rostro con mas area
            areas = f_detector.get_areas(boxes_face)
            index = np.argmax(areas)
            rectangles = rectangles[index]
            boxes_face = np.expand_dims(boxes_face[index],axis=0)
            # blinks_detector
            COUNTER,TOTAL = detector.eye_blink(gray,rectangles,COUNTER,TOTAL)
            # agregar bounding box
            img_post = f_detector.bounding_box(im,boxes_face,['blinks: {}'.format(TOTAL)])
        else:
            img_post = im
        #cv2.putText(img_post,f"FPS: {round(FPS,3)}",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('blink_detection',img_post)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if TOTAL == 2:
            cv2.destroyAllWindows()
            cap.release()
            return TOTAL


