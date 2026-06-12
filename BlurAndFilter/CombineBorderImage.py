import cv2
import numpy as np

# Load an image
image = cv2.imread(r"D:\Input.jpg")

# Define border thickness and color
border_thickness = 20
border_color = (0, 255, 0)  # Green color in BGR format

# Add a border around the image
border_image = cv2.copyMakeBorder(image, border_thickness, border_thickness,
                                  border_thickness, border_thickness,
                                  cv2.BORDER_REFLECT_101, value=border_color)
border_image1 = cv2.copyMakeBorder(image, border_thickness, border_thickness,
                                  border_thickness, border_thickness,
                                  cv2.BORDER_WRAP, value=border_color)

border_image3 = cv2.copyMakeBorder(image, border_thickness, border_thickness,
                                  border_thickness, border_thickness,
                                  cv2.BORDER_ISOLATED, value=border_color)

# Display the original and bordered images
cv2.imshow('Original Image', image)
cv2.imshow('Wrap Bordered Image', border_image1)
cv2.imshow('Refect Bordered Image', border_image)
cv2.imshow('Isolated Bordered Image', border_image3)
#cv2.imshow(' Transparent Bordered Image', border_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
