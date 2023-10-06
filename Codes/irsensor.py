import RPi.GPIO as GPIO
import time

sensor = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)



try: 
   while True:
      if GPIO.input(sensor):
          print("Object Detected")
      else:
          print("Object not Detected")


except KeyboardInterrupt:
    GPIO.cleanup()
