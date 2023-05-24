import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)                                                                                                    
toggle = 2
GPIO.setup(toggle, GPIO.OUT)
while True:
	GPIO.output(toggle, False)
