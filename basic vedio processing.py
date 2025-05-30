import cv2

def play_video_slow_fast(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    slow_factor = 2  # 2x slower
    fast_factor = 2  # 2x faster
    mode = 'normal'  # Modes: 'slow', 'fast', 'normal'
    frame_count = 0

    print("Press 's' for slow motion, 'f' for fast motion, 'n' for normal, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if mode == 'fast':
            # Skip frames to speed up video
            if frame_count % fast_factor == 0:
                cv2.imshow('Video Playback', frame)
                key = cv2.waitKey(int(1000 / fps)) & 0xFF
            else:
                key = cv2.waitKey(1) & 0xFF  # Minimal delay for skipped frames

        elif mode == 'slow':
            # Display frame longer
            cv2.imshow('Video Playback', frame)
            key = cv2.waitKey(int(1000 / fps * slow_factor)) & 0xFF

        else:  # Normal playback
            cv2.imshow('Video Playback', frame)
            key = cv2.waitKey(int(1000 / fps)) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('s'):
            mode = 'slow'
            print("Switched to slow motion.")
        elif key == ord('f'):
            mode = 'fast'
            print("Switched to fast motion.")
        elif key == ord('n'):
            mode = 'normal'
            print("Switched to normal speed.")

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file = r"C:\Users\vijay\Downloads\sample-vedio.mp4"
    play_video_slow_fast(video_file)
