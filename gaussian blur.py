import cv2

# Read the image from the file path (update path as needed)
image = cv2.imread(r"C:\Users\vijay\Downloads\avengers.jpeg")

if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Apply Gaussian blur
    # Parameters: (image, ksize, sigmaX)
    # ksize must be odd and positive, e.g., (15, 15)
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display the blurred image
    cv2.imshow("Blurred Image", blurred_image)

    # Save the blurred image to disk
    #cv2.imwrite("blurred_image.jpeg", blurred_image)
    #print("Blurred image saved as blurred_image.jpeg")

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
