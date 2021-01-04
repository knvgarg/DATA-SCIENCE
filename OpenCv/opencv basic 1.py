# simple program to read and show image
import cv2
img3 = cv2.imread('dog.png')
cv2.imshow('Dog Image', img3)
cv2.imshow('Dog Image', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()