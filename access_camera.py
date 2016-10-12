import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()

ap.add_argument("-v", "--video", required=False, help="path to the (optional) video file")
args = vars(ap.parse_args())

# if a video path was not supplied, grab the reference to the webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(0)
	print("Streaming from camera")

# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])
	print("reading", args["video"])

# keep looping
while True:
	# grab the current frame
	(success, frame) = camera.read()

	if success is False:
		print("End of stream")
		break

	cv2.imshow("Frame", frame)

	if cv2.waitKey(50) & 0xFF == ord('q'):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()