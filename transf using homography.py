import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Path to the input image
    image_path = r"C:\Users\vijay\Downloads\butterfly.jpeg"
    
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image from the path.")
        return

    height, width = img.shape[:2]

    # Define 4 source points from the image (you can adjust these points)
    src_pts = np.array([
        [100, 100],        # Top-left corner
        [width - 100, 100],  # Top-right corner
        [100, height - 100], # Bottom-left corner
        [width - 100, height - 100]  # Bottom-right corner
    ], dtype=np.float32)

    # Define 4 destination points for the transformation
    dst_pts = np.array([
        [0, 0],            # Top-left corner in the transformed image
        [width, 0],       # Top-right corner
        [0, height],      # Bottom-left corner
        [width, height]   # Bottom-right corner
    ], dtype=np.float32)

    # Compute the homography matrix
    H, status = cv2.findHomography(src_pts, dst_pts)

    # Apply the perspective transformation
    transformed_img = cv2.warpPerspective(img, H, (width, height))

    # Convert BGR to RGB for displaying with matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    transformed_rgb = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB)

    # Plot original and transformed images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img_rgb)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Transformed Image using Homography')
    plt.imshow(transformed_rgb)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
