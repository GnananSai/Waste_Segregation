import RPi.GPIO as GPIO
from time import sleep

def stepper_movement(new_bin_no , current_bin_no):
	each_bin_steps =67
	if(new_bin_no == current_bin_no):
		return current_bin_no
		
	# Direction pin from controller
	DIR = 10
	#Step pin from controller
	STEP = 8
	# 0/1 used to signify clockwise or counterclockwise.
	CW = 1
	CCW = 0
	# Setup pin layout on PI
	GPIO.setmode(GPIO.BOARD)

	# Establish Pins in software
	GPIO.setup(DIR, GPIO.OUT)
	GPIO.setup(STEP, GPIO.OUT)
	GPIO.output(DIR, CW)

	if(current_bin_no ==0):
		if(new_bin_no == 1):
			sleep(1.0)
			# Makeit go clockwise
			GPIO.output(DIR,CW)
		else:
			sleep(1.0)
			#Make it go anti_clockwise
			GPIO.output(DIR, CCW)
	else if(current_bin_no == 1):
		if(new_bin_no == 0):
			sleep(1.0)
			#Make it go anti_clockwise
			GPIO.output(DIR, CCW)
		else:
			sleep(1.0)
			# Makeit go clockwise
			GPIO.output(DIR,CW)
	else:
		if(new_bin_no == 0):
			sleep(1.0)
			# Makeit go clockwise
			GPIO.output(DIR,CW)
		else:
			sleep(1.0)
			#Make it go anti_clockwise
			GPIO.output(DIR, CCW)
	for x in range(each_bin_steps):
			# Set one coil winding to high
			GPIO.output(STEP,GPIO.HIGH)
			# Allow it to get there.
			sleep(.005) # Dictates how fast stepper motor will run
			# Set coil winding to low
			GPIO.output(STEP,GPIO.LOW)
			sleep(.005) # Dictates how fast stepper motor will run
	GPIO.cleanup()	
	return new_bin_no	
		
	
			
			
		
		
	
		
			
