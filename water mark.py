import cv2
from matplotlib import pyplot as plt

# Using forward slashes in the file path
img = cv2.imread("C:/Users/vijay/Downloads/butterfly1.jpeg", cv2.IMREAD_GRAYSCALE)
watermarked = img.copy()

cv2.putText(watermarked,'VIJAY-IMG', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (255), 2, cv2.LINE_AA)

plt.imshow(watermarked, cmap='gray')
plt.title('Watermarked Image')
plt.axis('off')
plt.show()
