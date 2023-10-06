import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
chanlist =(40,38)
p = GPIO.PWM(chanlist, 100)
x=1 #has to change
p.start(x)

p.ChangeDutyCycle(2.5)
time.sleep(x)
p.ChangeDutyCycle(11.5) # may need to be adjusted
time.sleep(x)
p.ChangeDutyCycle(20.5)
time.sleep(x)
p.ChangeDutyCycle(11.5) # may need to be adjusted

GPIO.cleanup()
