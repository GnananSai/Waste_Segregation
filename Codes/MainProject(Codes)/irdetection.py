


def irdetection():
	import RPi.GPIO as GPIO
	import time
	sensor1 =  12 #has to be changed

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sensor1,GPIO.IN)

	try: 
		if GPIO.input(sensor1):
			counter =True
		else:
			counter =False
		GPIO.cleanup()
		return counter
	except:
		GPIO.cleanup()
		
