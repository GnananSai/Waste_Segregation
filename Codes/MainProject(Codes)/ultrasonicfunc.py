

def ultrasonic():
	import RPi.GPIO as GPIO
	import time
	GPIO.setmode(GPIO.BCM)
	trigPin= 7	#Trigger oin
	echoPin= 1		#Receiving pin
	GPIO.setup(trigPin, GPIO.OUT)	
	GPIO.setup(echoPin, GPIO.IN)
	empty = 900		#Have to change its some random value for now.(Value when the bin is empty)
	end_time = time.time()+5;
	n=0
	avg=0
	try:
		while True:
			if time.time()>end_time:
				break
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
			#print(int(timetaken*1E6))
			n+=1
			avg += int(timetaken*1E6)
		GPIO.cleanup()
		return (avg/n)
	except:
		GPIO.cleanup()
