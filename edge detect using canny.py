import cv2
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

    # Perform Canny edge detection
    # You can adjust the thresholds as needed
    edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)

    # Plot original and edge-detected images
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Canny Edge Detection')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
