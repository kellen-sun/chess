import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
control1 = 2
control2 = 3
control3 = 4
GPIO.setup(control1, GPIO.OUT)
GPIO.setup(control2, GPIO.OUT)
GPIO.setup(control3, GPIO.OUT)

toggle = 17
GPIO.setup(toggle, GPIO.OUT)

readinput = [27, 22, 10, 9, 11, 5, 6, 13]
for i in readinput:
	GPIO.setup(i, GPIO.IN)

piece_location = []

