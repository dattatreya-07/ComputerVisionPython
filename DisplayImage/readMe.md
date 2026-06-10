To display an image using OpenCV in Python, you can use the cv2.imshow() function.It 
takes two arguments: the window name and the image you want to display. After displaying 
the image, you should use cv2.waitKey() to wait for a key event and 
cv2.destroyAllWindows() to close the display window. Begin by importing the OpenCV 
library in your Python script using import cv2. Use the cv2.imread() function to load an 
image from the file system. Provide the path to the image as an argument. After loading the 
image, check if it's valid using a simple conditional statement to ensure it was read 
successfully. Utilize the cv2.imshow() function to display the loaded image in a window. 
Remember to add a delay using cv2.waitKey() to keep the window open.After displaying the 
image, release resources and close the window using cv2.destroyAllWindows(). To write and 
save the loaded file  Using of  cv2.imwrite() function.
