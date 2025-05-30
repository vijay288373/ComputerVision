import cv2
from matplotlib import pyplot as plt

# Use escaped backslashes in the file path
img = cv2.imread('C:\Users\vijay\Downloads\butterfly1.jpeg',cv2.IMREAD_GRAYSCALE)

# Crop area
cropped = img[50:150, 100:200]  
img_copy = img.copy()

# Paste the cropped image elsewhere
img_copy[200:300, 300:400] = cropped  

# Display the image
plt.imshow(img_copy, cmap='gray')
plt.title('Crop & Paste')
plt.axis('off')
plt.show()
