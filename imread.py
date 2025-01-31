import cv2

print(cv2.__version__)

# Read the image
img = cv2.imread(r'fff.jpeg', 1)
print(img)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image")
else:
    # Display the image
    cv2.imshow("Image Window", img)

    # Wait for a key press indefinitely or for a given amount of time
    cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()
