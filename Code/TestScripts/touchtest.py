import time
import board
import digitalio
try:
    import RPi.GPIO as GPIO
except ImportError:
    import _fake_GPIO as GPIO

print("hello touch!")

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def touch_callback(channel):
    if channel == 2:
        print("Button 4 touch detected!")
    elif channel == 3:
        print("Button 3 touch detected!")
    elif channel == 4:
        print("Button 1 touch detected!")
    elif channel == 17:
        print("Button 2 touch detected!")
    else:
        print("Toch detected in unknown channel " + str(channel) + "!")

GPIO.add_event_detect(2, GPIO.FALLING, callback=touch_callback)
GPIO.add_event_detect(3, GPIO.FALLING, callback=touch_callback)
GPIO.add_event_detect(4, GPIO.FALLING, callback=touch_callback)
GPIO.add_event_detect(17, GPIO.FALLING, callback=touch_callback)

while True:
    #print(GPIO.input(2), GPIO.input(3), GPIO.input(4), GPIO.input(14))
    time.sleep(0.5)
