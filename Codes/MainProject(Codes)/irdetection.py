import RPi.GPIO as GPIO
import time


def irdetection():
	sensor1 = 23
	sensor2 = 24

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sensor1,GPIO.IN)
	GPIO.setup(sensor2,GPIO.IN)

	try: 
		if GPIO.input(sensor1) or GPIO.input(sensor2):
			counter =True
			#print "Object Detected"
			while GPIO.input(sensor1) or GPIO.input(sensor2):
				time.sleep(0.2)
		else:
			counter =False
		GPIO.cleanup()
		return counter
		
