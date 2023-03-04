#importing the cv2 library
import cv2

#reading the colourful jpg format image that is to be sketched
image = cv2.imread("bear.jpg")
cv2.imshow("Bear", image)
cv2.waitKey(0)

#converting the colourful image to gray_image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Image", gray_image)
cv2.waitKey(0)

#inverting the gray_image
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey(0)

#converting the inverted image to blur image using the Gaussian Function in OpenCV
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#dividing the gray_image with inverted_blurred image to get pencil_sketch look of colourful image
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
