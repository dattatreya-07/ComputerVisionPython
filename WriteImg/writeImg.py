import cv2
image = cv2.imread(r"C:\Users\Dattatreya\OneDrive\Pictures\325_ROG-Prism.jpg")
cv2.imwrite('output.png', image)  # Saves the image as a PNG file

