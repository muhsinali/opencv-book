# This is a class we made ourselves. It's a convenience class, 
# containing several basic image processing methods.

import numpy as np
import cv2

def translate(image, x, y):
	M = np.float32([[1, 0, x], [0, 1, y]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
	return shifted
