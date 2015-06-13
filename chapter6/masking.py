import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Image's pathname")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# create mask
rectangle = np.zeros(image.shape, dtype = "uint8")
cv2.rectangle(rectangle, (100, 0), (image.shape[1] - 100, image.shape[0]), (255, 255, 255), -1)
cv2.imshow("Mask", rectangle)

# perform AND bitwise operation
bitwiseAnd = cv2.bitwise_and(image, rectangle)
cv2.imshow("Mask Applied to Image", bitwiseAnd)
cv2.waitKey(0)

circle = np.zeros(image.shape, dtype = "uint8")
cv2.circle(circle, (150, 150), 100, (255, 255, 255), -1)
cv2.imshow("Circle Mask Applied to Image", cv2.bitwise_and(image, circle))
cv2.waitKey(0)
