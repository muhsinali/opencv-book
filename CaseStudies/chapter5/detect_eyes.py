from packages.eyetracker import EyeTracker
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required = True,
	help = "Face cascade classifier pathname")
ap.add_argument("-e", "--eye", required = True,
	help = "Eye cascade classifier pathname")
args = vars(ap.parse_args())

et = EyeTracker(args["face"], args["eye"])

with PiCamera() as camera:
	scalingFactor = 480.0 / 640
	width = 300
	height = int(scalingFactor * width)
	GREEN = (0, 255, 0)
	rawCapture = PiRGBArray(camera, size=(width, height))

	for frame in camera.capture_continuous(
			rawCapture, "bgr", True, (width, height)):
		image = frame.array
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		rectangles = et.track(gray)

		for (x1, y1, x2, y2) in rectangles:
			cv2.rectangle(image, (x1, y1), (x2, y2), GREEN, 2)
		cv2.imshow("Eye tracker", image)
		rawCapture.truncate(0)

		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
	cv2.destroyAllWindows()

