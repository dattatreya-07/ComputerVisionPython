import cv2

# Load an image
image = cv2.imread(r"D:\Input.jpg")
image1 = cv2.imread(r"D:\Input.jpg")
image2 = cv2.imread(r"D:\Input.jpg")
image3 = cv2.imread(r"D:\Input.jpg")
# Define the kernel size for average blur
kernel_size = (5, 5)

# Apply average blur
blurred_image = cv2.blur(image, kernel_size)
blurred_image1 = cv2.GaussianBlur(image1, (5, 5), 0)
blurred_image2 = cv2.medianBlur(image, 11)
blurred_image3 = cv2.bilateralFilter(image, 9, 75, 75)
# Display the original and blurred images
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Blurred Image1', blurred_image1)
cv2.imshow('Blurred Image2', blurred_image2)
cv2.imshow('Blurred Image3', blurred_image3)
cv2.waitKey(0)
cv2.destroyAllWindows()
