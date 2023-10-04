from detectionfunc import detection
from ultrasonicfunc import ultrasonic
from step_rotate import stepper_movement
from irdetection import irdetection
from servofunc import servo_rot

current_bin = 0
try:
	while True:
		if(irdetection()):
			new_bin = detection()
			if(new_bin ==3):
				continue
			current_bin = stepper_movement(current_bin, new_bin)
			servo_rot()
