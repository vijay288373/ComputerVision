import cv2

cap = cv2.VideoCapture('sample_video.mp4')
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play in reverse
for frame in reversed(frames):
    cv2.imshow('Reverse Video', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
