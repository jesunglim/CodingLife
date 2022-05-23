import cv2
import numpy as np

image1 = np.zeros((300, 300), np.uint8)
image2 = image1.copy()

h, w = image1.shape[:2]
cx, cy = w//2, h//2
cv2.circle(image1, (cx,cy), 100, 255, -1)

image6 = cv2.bitwise_not(image1)

cv2.imshow('image1', image1)
cv2.imshow('image6', image6)

cv2.waitKey(0)