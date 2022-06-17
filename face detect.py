import cv2

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("youtube_downloader/BLACKPINK - JISOO Forever Young FOCUSED CAMERA.mp4")
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

scaleFactor = 2
minNeighber = 4


while (cap.isOpened()):
     check, frame = cap.read()
     if check == True:
         # gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         face_detect = face_cascade.detectMultiScale(frame, scaleFactor, minNeighber)
         eyes_detect = eyes_cascade.detectMultiScale(frame, scaleFactor, minNeighber)
         # แสดงตำแหน่งที่เจอใบหน้า
         for (x, y, w, h) in face_detect:
             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
         for (x, y, w, h) in eyes_detect:
             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
         cv2.imshow("Output", frame)
         if cv2.waitKey(1) & 0xFF == ord("q"):
             break
     else :
         break

cap.release()
cv2.destroyAllWindows()