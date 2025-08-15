# import cv2

# video=cv2.VideoCapture(0)

# while True:
#     ret,frame=video.read()
#     cv2.imshow("Age-Gender",frame)
#     k=cv2.waitKey(1)
#     if k==ord('q'):
#         break
#     video.release()
#     cv2.destroyAllWindows()
import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break  # exit if there's an issue with the webcam
    
    cv2.imshow("Age-Gender", frame)

    # Wait for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources AFTER the loop
video.release()
cv2.destroyAllWindows()
