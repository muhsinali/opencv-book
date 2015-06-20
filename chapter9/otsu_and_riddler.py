import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("image", help = "Image pathname")
image = cv2.imread(vars(ap.parse_args())["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Original", image)

# Otsu thresholding
T = mahotas.thresholding.otsu(blurred)
print "Otsu's threshold: %d" % T
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh <= T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

# Riddler-Calvard thresholding
T = mahotas.thresholding.rc(blurred)
print "Riddler-Calvard: %d" % T
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh <= T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
