import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Path to the input image
    image_path = r"C:\Users\vijay\Downloads\butterfly1.jpeg"
    
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image from the path.")
        return

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel operator along the X-axis
    sobel_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)

    # Apply Sobel operator along the Y-axis
    sobel_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=5)

    # Calculate the magnitude of the gradient
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Convert the result to uint8
    sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)

    # Plot original and Sobel edge-detected images
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Sobel Edge Detection (XY-axis)')
    plt.imshow(sobel_magnitude, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
