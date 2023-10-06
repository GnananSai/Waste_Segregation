from detectionfunc import detection
from ultrasonicfunc import ultrasonic
from step_rotate import stepper_movement
from irdetection import irdetection
from servofunc import servo_rot
import RPi.GPIO as GPIO
import time

current_bin = 0
percentages= [0, 0, 0]
try:
	while True:
		#print("Ready to go")
		if(irdetection()):
			new_bin = detection()
			if(new_bin ==3):
				continue
			current_bin = stepper_movement(current_bin, new_bin)
			print("check1")
			#servo_rot() #Once forwad and Once backward (Have to change yet)
			perccentages[current_bin] = ultrasonic()
			print("check2")
			print(percentages[current_bin])
			#time.sleep(10)
except:
	GPIO.cleanup()
