OpenCV provides various draw functions that allow you to add different shapes and annotations to 
images. Some of the draw functions in OpenCV are cv2.line(), cv2.circle(), cv2.rectangle(). These 
functions allow you to add visual elements like lines, circles, and rectangles to your images using 
OpenCV. 

Drawing a Line in OpenCV :

To draw a line on an image using OpenCV, you can use the cv2.line() function. This function takes the 
image, starting and ending coordinates of the line, color, thickness, and other parameters as 
arguments.

Drawing a Circle in OpenCV:

To draw a circle on an image using OpenCV, you can use the cv2.circle() function. This 
function requires the image, center coordinates, radius, color, thickness, and other parameters. 

Drawing a Rectangle in OpenCV:
 
To draw a rectangle on an image using OpenCV, you can use the cv2.rectangle() function. 
This function takes the image, top-left and bottom-right corner coordinates, color, thickness, 
and other parameters.

Some other draw functions in OpenCV:

1. cv2.ellipse() 
Draws an ellipse on an image with specified center, axes lengths, angle, start and end angles, 
and other parameters,as shown in fig 2.5.1. 
2. cv2.polylines() 
Draws one or more polygons (closed curves) on an image. 
3. cv2.fillPoly() 
Fills one or more polygons with a specified color on an image. 
4. cv2.arrowedLine() 
Draws an arrowed line on an image with a specified starting and ending point.

Draw a text string in OpenCV :

Writes text on an image at a specified position in OpenCV we use the cv2.putText() function 
to draw the specified text string at the given position.

Contour:

Contours are continuous curves that represent the boundaries of objects in an image. In 
OpenCV, contour detection is a fundamental technique in image processing and computer 
vision. It's used to identify and extract shapes, objects, or regions of interest from an image. 

Drawing an Contours 
After finding the contours, you can draw them on an image using the cv2.drawContours() 
function. This function takes the image, a list of contours, the contour index (-1 to draw all 
contours), color, and thickness as arguments.This example code reads an image, converts it to 
grayscale, applies thresholding to create a binary image, finds contours, and draws them on a 
blank image. The final output displays both the original image and the image with drawn 
contours. Contour detection and drawing are essential techniques for tasks like object 
detection, image segmentation, and shape analysis in computer vision applications.
