from packages.face_detector import FaceDetector
from picamera import PiCamera
from picamera.array import PiRGBArray
import argparse, cv2, time

ap = argparse.ArgumentParser()
ap.add_argument("--cascade", default = "cascades/haarcascade_frontalface_default.xml", help = "Cascade XML file pathname")
args = vars(ap.parse_args())

fd = FaceDetector(args["cascade"])

with PiCamera() as camera:
        scalingFactor = 480.0 / 640     # 640x480 resolution
       	width = 300 
        height = int(scalingFactor * width)
       	rawCapture = PiRGBArray(camera, size=(width, height))
        time.sleep(0.5)

       	for output in camera.capture_continuous(rawCapture, format = "bgr", 
		use_video_port = True, resize=(width, height)):
                
		frame = output.array
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faceRects = fd.detect(gray)
		for (x, y, w, h) in faceRects:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.imshow("Face", frame)
	
		if cv2.waitKey(1) & 0xFF  == ord("q"):
			break
               	rawCapture.truncate(0)
cv2.destroyAllWindows()
