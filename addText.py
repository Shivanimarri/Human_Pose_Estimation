#import numpy as np
import cv2

# Define the font
font = cv2.FONT_HERSHEY_SIMPLEX

# Read the image
img = cv2.imread(r"fff.jpeg", 1)

# Add text to the image
cv2.putText(img, 'Shivani', (20, 45), font, 2, (0, 200, 140), 5)

# Display the image
cv2.imshow("image", img)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all the windows showing images
cv2.destroyAllWindows()
