import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Dattatreya\OneDrive\Pictures\325_ROG-Prism.jpg")
image1 = cv2.imread(r"C:\Users\Dattatreya\OneDrive\Pictures\Picture1.png")
image2 = cv2.imread(r"C:\Users\Dattatreya\OneDrive\Pictures\NPDA.jpg")
center = (450, 450)
radius = 125
start_point = (325, 325)
end_point = (575, 575)
start_point1 = (575, 575)
end_point1 = (325, 325)
color = (100, 255, 80)  
thickness = 3
cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow("line_drawn", image)
color = (255, 100, 80)
cv2.circle(image1, center, radius, color, thickness)
cv2.imshow('Circle_drawn', image1)
color = (100, 80, 255)
cv2.rectangle(image2, start_point, end_point, color, thickness)
cv2.imshow("Draw Rectangle", image2)
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Define text string and position
text = "Welcome to OpenCV!"
position = (90, 200)

# font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
color = (255, 255, 155)  
thickness = 3

# Draw the text on the image
cv2.putText(image, text, position, font, font_scale, color, thickness)

# Display the image
cv2.imshow('Text Drawing', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
