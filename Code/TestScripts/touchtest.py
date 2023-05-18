import time
import board
import digitalio
try:
    import RPi.GPIO as GPIO
except ImportError:
    import _fake_GPIO as GPIO

PinButton1 = 22
PinButton2 = 27
PinButton3 = 23
PinButton4 = 24

print("hello touch!")

GPIO.setmode(GPIO.BCM)

GPIO.setup(PinButton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PinButton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PinButton3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PinButton4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def touch_callback(channel):
    if channel == PinButton1:
        print("Button 1 touch detected!")
    elif channel == PinButton2:
        print("Button 2 touch detected!")
    elif channel == PinButton3:
        print("Button 3 touch detected!")
    elif channel == PinButton4:
        print("Button 4 touch detected!")
    else:
        print("Toch detected in unknown channel " + str(channel) + "!")

GPIO.add_event_detect(PinButton1, GPIO.FALLING, callback=touch_callback)
GPIO.add_event_detect(PinButton2, GPIO.FALLING, callback=touch_callback)
GPIO.add_event_detect(PinButton3, GPIO.FALLING, callback=touch_callback)
GPIO.add_event_detect(PinButton4, GPIO.FALLING, callback=touch_callback)

while True:
    # print(GPIO.input(PinButton1), GPIO.input(PinButton2), GPIO.input(PinButton3), GPIO.input(PinButton4))
    time.sleep(0.5)
