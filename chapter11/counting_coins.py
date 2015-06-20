import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("image", help = "Image pathname")
image = cv2.imread(vars(ap.parse_args())["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

print "I count %d coins in this image" % len(cnts)

coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

cv2.destroyAllWindows()

all_images = np.hstack((image, coins))
cv2.imshow("Contours", all_images)
cv2.waitKey(0)

for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)

	print "Coin #%d" % (i + 1)
	coin = image[y:y + h, x: x + w]
	cv2.imshow("Coin", coin)

	mask = np.zeros(image.shape[:2], dtype = "uint8")
	(center, radius) = cv2.minEnclosingCircle(c)
	cv2.circle(mask, tuple(map(int, center)), int(radius), 255, -1)
	mask = mask[y:y + h, x:x + w]

	cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	cv2.waitKey(0)




