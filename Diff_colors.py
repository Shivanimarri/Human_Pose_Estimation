# Importing the OpenCV module
import cv2

# Reading the image 'Gan.jpeg' in color mode (1)
img = cv2.imread('fff.jpeg', 1)

# Printing the image matrix
print(img)

# Converting the image to grayscale
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Converting the image from BGR to RGB
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Converting the image from BGR to HSV
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Converting the image from BGR to LAB
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Displaying the color image
cv2.imshow("Color Image", img)

# Displaying the grayscale image
cv2.imshow("Gray Image", img1)

# Displaying the RGB image
cv2.imshow("RGB Image", img2)

# Displaying the HSV image
cv2.imshow("HSV Image", img3)

# Displaying the LAB image
cv2.imshow("LAB Image", img4)

# Waiting indefinitely until a key is pressed
cv2.waitKey(0)

# Closing all OpenCV windows
cv2.destroyAllWindows()
