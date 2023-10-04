import RPi.GPIO as GPIO
from time import sleep

def get_pwm(angle):
    return (angle/18.0) + 2.5


def servo_rot():
	GPIO.setmode(GPIO.BCM)
	pwmPin = 18
	GPIO.setup(pwmPin, GPIO.OUT)
	pwm = GPIO.PWM(pwmPin, 50)
	pwm.start(0)
	i=0
	try:
		#angle = float(input('angle: '))
		pwmPercent = get_pwm(360)
		pwm.ChangeDutyCycle(pwmPercent)
		sleep(.1)
		GPIO.cleanup()
		return
