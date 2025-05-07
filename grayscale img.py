import cv2

# Use raw string for Windows file path to avoid escape character issues
image = cv2.imread(r"C:\Users\vijay\Downloads\avengers.jpeg")

if image is None:
    print('Error: Image not found or unable to load.')
else:
    # Display the original image
    cv2.imshow('Original Image', image)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)

    # Save the grayscale image in the current directory
    cv2.imwrite('grayscale_image.jpeg', gray_image)
    print('Image has been converted to grayscale and saved as grayscale_image.jpeg')

    # Wait for a key press and then close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
