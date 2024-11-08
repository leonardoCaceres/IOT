import cv2

cam = cv2.VideoCapture(0)

detec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(frame_width)
print(frame_height)

odd = True

def get_middle(x,y,x1,y1):
	return int((x+x1)/2), int((y+y1)/2)

while True:
	ret, frame = cam.read()

	if odd:
		cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		face = detec.detectMultiScale(cinza, 1.3, 3)
		i = 0
		for (x, y, larg, alt) in face: #Desenhar o retângulo
			cv2.rectangle(frame, (x, y), (x + larg, y + alt), (0, 255, 0), 3)
			cx, cy = get_middle(x, y, x + larg, y + alt)
			cv2.circle(frame, (cx, cy), 30, (0, 0, 255), 3)
			
		cv2.imshow('Camera', frame)
		if cv2.waitKey(1) == ord('q'):
			break
	odd = not odd

cam.release()
cv2.destroyAllWindows()
