import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original cool image", image)

b, g, r = image[0, 0]
print "first R: %d G: %d B: %d" % (r, g, b)

image[0, 0] = (0, 0, 255)
b, g, r = image[0, 0] 
print "adjusted R: %d G: %d B: %d" % (r, g, b)

corner = image[0:100, 0:200]
cv2.imshow("Cropped corner", corner)
image[0:250, 0:100] = (0, 0, 255)
image[125, 50] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
