"""
https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

configure raspberry pi pin for servo motor control
- raspberry pi 3 model B+

duty cycle (dc) takes value between (0-100)

servo.start(dc)           # start PWM at dc
servo.ChangeDutyCycle(dc) # changes duty cycle to dc
servo.stop()              # stops PWM

servo motor basically moves to and holds at given rotation based on
supplied pulse train duty cycle
"""
import time
import RPi.GPIO as GPIO

servo_ctrl = 12

GPIO.setmode(GPIO.BCM) # use logical pin names vs board pins
GPIO.setup(servo_ctrl, GPIO.OUT) # configure servo_ctrl pin as output

servo1 = GPIO.PWM(servo_ctrl, 50) # (channel, frequency)
servo1.start(0)
time.sleep(1)

print ("starting sequence")

def move_arm(val: int) -> None:
    print ("current setting: {}".format(val))
    servo1.ChangeDutyCycle(val)
    time.sleep(0.5)

    servo1.ChangeDutyCycle(0) # to reduce jitter
    time.sleep(1)

def flush() -> None:
    # start upright at 90 degrees
    move_arm(8)

    # move down to 0 degrees
    move_arm(4)
    time.sleep(1)

    # return to idle position
    move_arm(8)

# range of motor limited between 2-12% duty cycle
# slightly less than 270 degree travel

#for i in range(2, 13):
#    move_arm(i)
#move_arm(2)
#time.sleep(1)

flush()

print ("shutting down")
servo1.stop()
GPIO.cleanup()
print ("exiting!")
