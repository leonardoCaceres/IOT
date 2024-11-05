import cv2

cam = cv2.VideoCapture(0)

detec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

odd = True

while True:
	ret, frame = cam.read()

	if odd:
		cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		face = detec.detectMultiScale(cinza, 1.3, 3)

		for (x, y, larg, alt) in face: #Desenhar o retângulo
			ret = cv2.rectangle(frame, (x, y), (x + larg, y + alt), (0, 255, 0), 3)

		cv2.imshow('Camera', frame)
		if cv2.waitKey(1) == ord('q'):
			break
	odd = not odd

cam.release()
cv2.destroyAllWindows()
