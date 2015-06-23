import cv2

class EyeTracker:
	def __init__(self, faceCascadePath, eyeCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
		self.eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

	def track(self, image):
		faceRects = self.faceCascade.detectMultiScale(
			image,
			scaleFactor = 1.2,
			minNeighbors = 5,
			flags = cv2.cv.CV_HAAR_SCALE_IMAGE,
			minSize = (30, 30)
			)
		rects = []

		for (fX, fY, fW, fH) in faceRects:
			rects.append((fX, fY, fX+fW, fY+fH))
			faceRegion = image[fY:fY+fH, fX:fX+fW]

			# detect eyes in faceRegion
			eyeRects = self.eyeCascade.detectMultiScale(
				faceRegion,
				scaleFactor = 1.1,
				minNeighbors = 10,
				flags = cv2.cv.CV_HAAR_SCALE_IMAGE,
				minSize = (20, 20)
			)

			for (eX, eY, eW, eH) in eyeRects:
				rects.append((
					fX+eX,
					fY+eY,
					fX+eX+eW,
					fY+eY+eH
					))
		return rects

