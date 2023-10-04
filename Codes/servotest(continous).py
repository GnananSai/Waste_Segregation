import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, 100)
p.start(5)

p.ChangeDutyCycle(2.5)
time.sleep(5)
p.ChangeDutyCycle(11.5) # may need to be adjusted
time.sleep(5)
p.ChangeDutyCycle(20.5)
time.sleep(5)
p.ChangeDutyCycle(11.5) # may need to be adjusted

GPIO.cleanup()
