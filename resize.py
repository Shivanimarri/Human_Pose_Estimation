import cv2

# Read the image
img = cv2.imread(r'fff.jpeg', 1)

# Print the original dimensions of the image
print('Original Dimensions:', img.shape)

# Specify the new dimensions for resizing
width = 350
height = 450
dim = (width, height)  # Corrected this line

# Resize the image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Print the resized dimensions of the image
print('Resized Dimensions:', resized.shape)

# Display the original and resized images
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized)

# Wait indefinitely until a key is pressed
cv2.waitKey(1000)

# Destroy all the windows
cv2.destroyAllWindows()
