import cv2

# Read the image from the file path (update the path as necessary)
image = cv2.imread(r"C:\Users\vijay\Downloads\avengers.jpeg")

if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert to grayscale as Canny works on single channel images
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    # Thresholds can be adjusted for different edge sensitivities
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

    # Display the Canny edge image
    cv2.imshow("Canny Edge Image", edges)

    # Save the edge image to disk
    cv2.imwrite("canny_edge_image.jpeg", edges)
    print("Canny edge image saved as canny_edge_image.jpeg")

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
