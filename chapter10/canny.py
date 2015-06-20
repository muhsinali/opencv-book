import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("image", help = "Image pathname")
image = cv2.imread(vars(ap.parse_args())["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
