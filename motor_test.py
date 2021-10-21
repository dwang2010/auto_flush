"""
https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

configure raspberry pi pin for servo motor control

duty cycle (dc) takes value between (0-100)

servo.start(dc)           # start PWM at dc
servo.ChangeDutyCycle(dc) # changes duty cycle to dc
servo.stop()              # stops PWM

servo motor basically moves to and holds at given rotation based on
supplied pulse train duty cycle
"""
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # use header pin numbering
GPIO.setup(16, GPIO.OUT) # configure pin 16 as output

servo = GPIO.PWM(16, 50) # (channel, frequency)
servo.start(0)

for i in range(5):
    servo.ChangeDutyCycle(40)
    time.sleep(1)

    servo.ChangeDutyCycle(20)
    time.sleep(1)

servo.stop()
GPIO.cleanup()
