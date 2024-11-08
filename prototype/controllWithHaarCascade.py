import cv2
import controll_start
import math

cam = cv2.VideoCapture(0)

detec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

center_x = frame_width/2
center_y = frame_height/2

odd = True

def get_middle(x,y,x1,y1):
	return int((x+x1)/2), int((y+y1)/2)

cx = 0
cy = 0
while True:
	ret, frame = cam.read()

	if odd:
		cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		face = detec.detectMultiScale(cinza, 1.3, 3)
		i = 0
		for (x, y, larg, alt) in face: #Desenhar o retângulo
			cv2.rectangle(frame, (x, y), (x + larg, y + alt), (0, 255, 0), 3)
			cx, cy = get_middle(x, y, x + larg, y + alt)
			
		if abs(cx - center_x) > 30:
			###ON THE RIGHT OF THE CENTER
			if cx > center_x:
				backwards(steps, hor)
			###ON THE LEFT OF THE CENTER
			else:
				forward(steps, hor)

		if abs(cy - center_y) > 30:
			###ON THE TOP OF THE CENTER
			if cy < center_y:
				backwards(steps, ver)
			###ON THE BELOW OF THE CENTER
			else:
				forward(steps, ver)
			forward(steps, ver)
			
		cv2.imshow('Camera', frame)
		if cv2.waitKey(1) == ord('q'):
			break
	odd = not odd

GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()


