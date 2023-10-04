import RPi.GPIO as GPIO
import time

sensor = 16


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)



try: 
   while True:
      if GPIO.input(sensor):
          print("Object not Detected")
      else:
          print("Object Detected")


except KeyboardInterrupt:
    GPIO.cleanup()
