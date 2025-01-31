import cv2

# Read image
img = cv2.imread('fff.jpeg', 1)

# Get the dimensions of the image
dimensions = img.shape

# Extract height, width, and number of channels
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

# Get the size of the image
size1 = img.size

# Print dimensions, height, width, number of channels, and size
print('Image Dimension:', dimensions)
print('Image Height:', height)
print('Image Width:', width)
print('Number of Channels:', channels)
print('Image Size:', size1)

# Split the image into its color channels
b, g, r = cv2.split(img)

# Merge the color channels back in BGR and RGB orders
merged_img_bgr = cv2.merge((b, g, r))
merged_img_rgb = cv2.merge((r, g, b))

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)
cv2.imshow('Merged BGR', merged_img_bgr)
cv2.imshow('Merged RGB', merged_img_rgb)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
