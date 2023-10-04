from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='10.0.0.164')

servo1 = Servo(17, min_pulse_width=.5/1000, max_pulse_width=2.5/1000, frame_width=20/1000, pin_factory=factory)

servo1.value = .95
servo1.value = -.95
