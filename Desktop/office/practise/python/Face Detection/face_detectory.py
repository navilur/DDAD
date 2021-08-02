import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Webcam
webcam = cv2.VideoCapture(0)

# Iterate Frames
while True:

     # Read The Current Frames
     frame_read , frame = webcam.read()
     grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

     # Detect Face
     face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

     # Draw Rectangle
     for (x, y, w, h) in face_coordinates:
          cv2.rectangle(frame, (x, y),(x+w, y+h), (randrange(256), randrange(256), randrange(256)), 5)
     
     # Display Video
     cv2.imshow('Navilur Rahman Face Detector', frame)
     
     key = cv2.waitKey(1)

     #Stop Pressing Q
     if key==81 or key==113:
          break