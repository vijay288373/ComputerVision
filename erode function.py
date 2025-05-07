import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('C:/Users/vijay/Downloads/avengers.jpeg')

# Step 2: Convert the image to grayscale (optional, depending on your needs)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Define the kernel for erosion
kernel = np.ones((5, 5), np.uint8)  # You can change the size of the kernel

# Step 4: Erode the image
eroded_image = cv2.erode(gray_image, kernel, iterations=1)

# Step 5: Display the original and eroded images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Eroded Image', eroded_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
