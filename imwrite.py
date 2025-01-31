import cv2
img = cv2.imread(r'fff.jpeg', 0) 
print(img) 
status = cv2.imwrite('ganapathy.png',img) 
print("Image written to file system: ", status)