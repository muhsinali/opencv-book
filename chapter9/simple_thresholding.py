import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("image", help = "Image Pathname")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Greyscale", image)


threshold = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)[1]
threshold_inv = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold Binary", threshold)
cv2.imshow("Threshold Binary Inverse", threshold_inv)

# Apply threshold_inv as a mask to image to only show the coins
cv2.imshow("Coins", cv2.bitwise_and(image, threshold_inv))
cv2.waitKey(0)
