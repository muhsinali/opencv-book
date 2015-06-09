import numpy as np
import cv2
# dtype = data type, uint8 = 8-bit unsigned integer
canvas = np.zeros((300, 300, 3), dtype = "uint8")

green = 0, 255, 0
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = 0, 0, 255
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (0, canvas.shape[0] / 2)
print "\n %d \t %d \n" % (centerX, centerY)
white = (255, 255, 255)

for r in xrange(0, 175, 25):
	cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

for i in xrange(0, 25):
	radius = np.random.randint(5, high = 200)
	color = np.random.randint(0, high = 256, size = (3,)).tolist()
	pt = np.random.randint(0, high = 300, size = (2,))
	cv2.circle(canvas, tuple(pt), radius, color, -1)
print pt, type(pt)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)



