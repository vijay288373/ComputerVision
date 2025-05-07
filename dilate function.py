import cv2
import numpy as np

# Read the image from the file path (update path accordingly)
image = cv2.imread(r"C:\Users\vijay\Downloads\avengers.jpeg")

if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert the image to grayscale (dilation typically applied on single channel mask)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection or threshold to get a binary image for dilation (optional but often needed)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Define the kernel for dilation
    kernel = np.ones((5,5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(binary, kernel, iterations=1)

    # Display the dilated image
    cv2.imshow("Dilated Image", dilated)

    # Save the dilated image
    cv2.imwrite("dilated_image.jpeg", dilated)
    print("Dilated image saved as dilated_image.jpeg")

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
