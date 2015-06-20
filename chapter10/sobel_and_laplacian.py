import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("image", help = "Image pathname")
image = cv2.imread(vars(ap.parse_args())["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Laplacian operator
lap = cv2.Laplacian(image, cv2.CV_64F)	# the 2nd argument is a data type, more specifically a 64-bit float data type. Note that the values stored here as integers but they're stored as a float data type.
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

# Sobel operator
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)	# detects vertical edges
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)	# detects horiz edges

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)
