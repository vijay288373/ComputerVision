import cv2
import numpy as np

def main():
    # Path to the input video
    video_path = r"C:\Users\vijay\Downloads\sample-vedio.mp4"
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return
    
    # Get video frame width, height and fps
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Define the four source points from the original video frames
    # Adjust these points according to the content of the video
    pts_src = np.float32([
        [100, 100],        # Top-left corner in original frame
        [width-100, 100],  # Top-right corner
        [100, height-100], # Bottom-left corner
        [width-100, height-100]  # Bottom-right corner
    ])
    
    # Define the four destination points for perspective transform
    # This example maps the points to the full frame size
    pts_dst = np.float32([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ])
    
    # Compute the perspective transform matrix
    matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
    
    # Define codec and create VideoWriter object to save the output if needed
    # Uncomment below lines to save output video
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    # out = cv2.VideoWriter('output_transformed.mp4', fourcc, fps, (width, height))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Apply perspective transform to the frame
        transformed_frame = cv2.warpPerspective(frame, matrix, (width, height))
        
        # Show original and transformed frames side by side
        combined = cv2.hconcat([frame, transformed_frame])
        cv2.imshow('Original (Left) | Transformed (Right)', combined)
        
        # Write the transformed frame if saving video
        # out.write(transformed_frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    # out.release()  # release writer if video saved
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

