import RPi.GPIO as GPIO
import time
from pygame import mixer
def dist():
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 16
      PIN_ECHO = 18

      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print("Waiting for sensor to settle")

      time.sleep(1)

      print ("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      pulse_start_time=0;
      pulse_end_time=0;
      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print ("Distance:",distance,"cm")
      Dist_int=int(distance)
      if(Dist_int<30):
          mixer.init()
          alert=mixer.Sound('bell.wav')
          alert.play()
      
while(True):
    dist()
