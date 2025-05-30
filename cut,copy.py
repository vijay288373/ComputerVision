import cv2
# Load images
source_image = cv2.imread('C:/Users/vijay/Downloads/butterfly1.jpeg')
destination_image = cv2.imread('C:/Users/vijay/Downloads/butterfly.jpeg')
# Crop the source image (x1, y1, width, height)
x1, y1, w, h = 100, 100, 200, 200
cropped_image = source_image[y1:y1+h, x1:x1+w]
# Paste the cropped image into the destination image
destination_image[y1:y1+h, x1:x1+w] = cropped_image
# Show result
cv2.imshow('Pasted Image', destination_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
