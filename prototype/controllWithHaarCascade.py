import cv2
from controll_start import *
import math
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Short sample app")
parser.add_argument("--cam-index", action="store", dest="cam_index", default=0)
args = parser.parse_args()

cam = cv2.VideoCapture(args.cam_index)

detec = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

center_x = frame_width / 2
center_y = frame_height / 2

odd = True


def get_middle(x, y, x1, y1):
    return int((x + x1) / 2), int((y + y1) / 2)


face_x = 0
face_y = 0
while True:
    ret, frame = cam.read()

    # if odd:
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = detec.detectMultiScale(cinza, 1.3, 3)
    if isinstance(face, np.ndarray):
        for x, y, larg, alt in face:  # Desenhar o retângulo
            cv2.rectangle(frame, (x, y), (x + larg, y + alt), (0, 255, 0), 3)
            face_x, face_y = get_middle(x, y, x + larg, y + alt)
            print(face_x, face_y)

        if abs(face_x - center_x) > 40:
            ###ON THE RIGHT OF THE CENTER
            if face_x < center_x:
                backwards(steps, hor)
            ###ON THE LEFT OF THE CENTER
            else:
                forward(steps, hor)

        if abs(face_y - center_y) < 40:
            ###ON THE TOP OF THE CENTER
            if face_y > center_y:
                backwards(steps, ver)
            ###ON THE BELOW OF THE CENTER
            else:
                forward(steps, ver)

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break
    # odd = not odd

GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()
