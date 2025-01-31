import numpy as np
import cv2

# Drawing a circle
img_circle = cv2.imread(r"fff.jpeg", 1)
cv2.circle(img_circle, (80, 80), 55, (0, 255, 0), -1)
cv2.imshow('Image with Circle', img_circle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Drawing a rectangle
img_rectangle = cv2.imread(r"fff.jpeg", 1)
cv2.rectangle(img_rectangle, (15, 25), (200, 150), (0, 255, 255), 5)
cv2.imshow('Image with Rectangle', img_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Drawing an ellipse
img_ellipse = cv2.imread(r"fff.jpeg", 1)
cv2.ellipse(img_ellipse, (150, 50), (80, 20), 5, 0, 360, (0, 0, 255), -1)
cv2.imshow('Image with Ellipse', img_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Drawing a line
img_line = cv2.imread(r"fff.jpeg", 1)
cv2.line(img_line, (10, 0), (150, 150), (0, 0, 0), 15)
cv2.imshow('Image with Line', img_line)
cv2.waitKey(0)
cv2.destroyAllWindows()
