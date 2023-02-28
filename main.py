import cv2

capture_obj = cv2.VideoCapture("car_passing.mp4")

while True:
	ret, frame = capture_obj.read()

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(30)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()