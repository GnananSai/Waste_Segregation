import RPi.GPIO as GPIO
from time import sleep

def get_pwm(angle):
    return (angle/36.0) + 2.5
GPIO.setmode(GPIO.BCM)
pwmPin = 18
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50)
pwm.start(0)

try:
	while True:
		angle = float(input('angle: '))
		pwmPercent = get_pwm(angle)
		pwm.ChangeDutyCycle(pwmPercent)
		sleep(.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('GOod to go')
