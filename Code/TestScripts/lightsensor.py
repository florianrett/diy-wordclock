import time
import board
import digitalio
try:
    import RPi.GPIO as GPIO
except ImportError:
    import _fake_GPIO as GPIO

print("hello light!")

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def light_callback(value):
	print("Lighting changed: ", GPIO.input(24))

GPIO.add_event_detect(24, GPIO.BOTH, callback=light_callback)

# sensor = digitalio.DigitalInOut(board.D17)
# sensor.direction = digitalio.Direction.INPUT
# sensor.pull = digitalio.Pull.DOWN


# GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# try:
# 	GPIO.wait_for_edge(17, GPIO.FALLING)
# 	print("falling edge ")
# except KeyboardInterrupt:
# 	GPIO.cleanup()


while True:
#	print(sensor.value)
	time.sleep(1)
