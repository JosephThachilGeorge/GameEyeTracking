import numpy as np
import cv2

face_cascade = cv2 . CascadeClassifier (’
haarcascade_frontalface_default .xml ’)
cap = cv2 . VideoCapture (0)

while 1:

# imagine

ret , img = cap . read ()

if ret == True :
gray = cv2 . cvtColor ( img , cv2 . COLOR_BGR2GRAY )

# face recognition

faces = face_cascade . detectMultiScale ( gray , 1.3 , 5)
eye_cascade = cv2 . CascadeClassifier (’ haarcascade_eye . xml ’
)
eyes = eye_cascade . detectMultiScale ( img ,1.3 ,10)

for (x ,y ,w , h ) in faces :

# x, y coordinates of the upper left point - w, h width and height

cv2 . rectangle ( img ,( x , y ) ,( x +w , y + h ) ,(255 ,0 ,0) ,2)

#blue rectangle
#eye recognition

for ( ex , ey , ew , eh ) in eyes :

#ex, ey, top left point coordinates - ew, eh width and height

cv2 . rectangle ( img , ( ex , ey ) , (( ex + ew ) ,( ey + eh ) ) ,
(0 ,0 ,255) ,1)

# red rectangle

cv2 . line ( img , ( ex , ey ) , (( ex + ew , ey + eh ) ) , (0 ,0 ,255) ,1)
#line for x
cv2 . line ( img , ( ex + ew , ey ) , (( ex , ey + eh ) ) , (0 ,0 ,255) ,1)

#line for x

cv2 . imshow (’img ’, img )
k = cv2 . waitKey (30) & 0 xff
if k == ord (’q’) :
break

cap . release ()
cv2 . destroyAllWindows ()
