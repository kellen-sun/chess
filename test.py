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
readinput = 27
GPIO.setup(readinput, GPIO.IN)


while True:
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, False)
	GPIO.output(control2, False)
	GPIO.output(control3, False)
	time.sleep(0.5)
	print(1, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, False)
	GPIO.output(control2, False)
	GPIO.output(control3, True)
	time.sleep(0.5)
	print(2, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, False)
	GPIO.output(control2, True)
	GPIO.output(control3, False)
	time.sleep(0.5)
	print(3, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, False)
	GPIO.output(control2, True)
	GPIO.output(control3, True)
	time.sleep(0.5)
	print(4, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, True)
	GPIO.output(control2, False)
	GPIO.output(control3, False)
	time.sleep(0.5)
	print(5, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, True)
	GPIO.output(control2, False)
	GPIO.output(control3, True)
	time.sleep(0.5)
	print(6, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, True)
	GPIO.output(control2, True)
	GPIO.output(control3, False)
	time.sleep(0.5)
	print(7, GPIO.input(readinput))
	
	GPIO.output(toggle, True)
	GPIO.output(toggle, False)
	GPIO.output(control1, True)
	GPIO.output(control2, True)
	GPIO.output(control3, True)
	time.sleep(0.5)
	print(8, GPIO.input(readinput))
	
