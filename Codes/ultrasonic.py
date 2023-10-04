import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trigPin=7
echoPin=1
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
try:
	while True:
		GPIO.output(trigPin,0)
		time.sleep(2E-6)
		GPIO.output(trigPin, 1) 	
		time.sleep(10E-6)
		GPIO.output(trigPin,0)
		while GPIO.input(echoPin)==0:
			pass
		echostarttime = time.time()
		while GPIO.input(echoPin)==1:
			pass
		echostoptime = time.time()
		timetaken = echostoptime-echostarttime
		print(int(timetaken*1E6))
		time.sleep(.2)
		
except KeyboardInterrupt():
	GPIO.cleanup()
	print("GPIO Good to go")
