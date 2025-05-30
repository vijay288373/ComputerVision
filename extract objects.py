import cv2

img = cv2.imread('C:/Users/vijay/Downloads/roko.jpeg')
roi = cv2.selectROI("Select Object", img)
cv2.destroyAllWindows()

x, y, w, h = roi
cropped = img[int(y):int(y+h), int(x):int(x+w)]

cv2.imshow('Extracted Object', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
