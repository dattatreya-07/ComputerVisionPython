Median Blur:

Median blur replaces each pixel's value with the median value of its neighboring pixels. It's 
effective in reducing salt-and-pepper noise while preserving edges. In Example code, the 
cv2.medianBlur() function is used to apply median blur to the input image. The 3 argument 
specifies the kernel size, which is the size of the neighborhood used for computing the 
median pixel value.

Bilateral Filter: 
The bilateral filter takes into account both spatial proximity and intensity similarity between 
pixels. It effectively blurs the image while preserving edges and fine details. 
Parameter Explanation:The input image you want to filter. Diameter of each pixel 
neighborhood that is used during filtering. A larger value means farther pixels will be 
considered in the calculation. A parameter that controls the color similarity weight. A smaller 
value means only pixels with similar colors will be considered. A parameter that controls the 
spatial similarity weight. A smaller value means only pixels within a close neighborhood will 
be considered. 
