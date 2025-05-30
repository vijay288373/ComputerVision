import cv2

def capture_webcam_with_speed():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 's' for SLOW motion")
    print("Press 'f' for FAST motion")
    print("Press 'q' to QUIT")

    speed = 1  # Default delay

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Webcam Stream", frame)

        key = cv2.waitKey(speed) & 0xFF

        if key == ord('s'):
            speed = 60  # Slow motion (longer delay)
            print("Switched to SLOW motion")
        elif key == ord('f'):
            speed = 10  # Fast motion (shorter delay)
            print("Switched to FAST motion")
        elif key == ord('q'):
            print("Quitting...")
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the function
capture_webcam_with_speed()
