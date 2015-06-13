import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

w, h = (image.shape[1], image.shape[0])
aspect_ratio = float(w) / h
new_height = 50.0
new_dimensions = (int(aspect_ratio * new_height), int(new_height))

resized = cv2.resize(image, new_dimensions, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized", resized)

resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)
