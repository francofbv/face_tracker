import cv2

###### constants #####
frameWidth = 640
frameHeight = 480
color = (255,0,255)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

##### set camera #####
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,100)

##### take input #####
while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    num_faces = face_cascade.detectMultiScale(img_gray,1.1,4)

    for (x,y,w,h) in num_faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
