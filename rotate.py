import cv2

# Read the image as greyscale
img = cv2.imread('fff.jpeg', cv2.IMREAD_GRAYSCALE)

# Get image height and width
(h, w) = img.shape[:2]

# Calculate the center of the image
center = (w / 2, h / 2)

# Rotation angles and scale
angle90 = 90
angle180 = 180
angle270 = 270
scale = 1.0

# Perform the counterclockwise rotation holding at the center
# 90 degrees rotation
M90 = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M90, (w, h))

# 180 degrees rotation
M180 = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M180, (w, h))

# 270 degrees rotation
M270 = cv2.getRotationMatrix2D(center, angle270, scale)
rotated270 = cv2.warpAffine(img, M270, (w, h))

# Display the original image
cv2.imshow('Original Image', img)

# Display the image rotated by 90 degrees
cv2.imshow('Image rotated by 90 degrees', rotated90)

# Display the image rotated by 180 degrees
cv2.imshow('Image rotated by 180 degrees', rotated180)

# Display the image rotated by 270 degrees
cv2.imshow('Image rotated by 270 degrees', rotated270)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all the windows showing images
cv2.destroyAllWindows()
