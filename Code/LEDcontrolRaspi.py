import time
import threading
from threading import Event
import board
import neopixel
import adafruit_tsl2591
try:
    import RPi.GPIO as GPIO
except ImportError:
    import _fake_GPIO as GPIO
import config

# NeoPixel connection Pin
pixel_pin = board.D21

# Number of pixels
num_pixels = 228

# LED strip color order
ORDER = neopixel.GRB

class controller:

    pixels = None
    lightsensor = None
    
    OnButton1 = None
    OnButton2 = None
    OnButton3 = None
    OnButton4 = None
    OnButton4_released = None
    OnLightlevelChanged = None
    
    # use threaded polling for light sensor
    LightSensorPollingThread = None
    PollingThreadInterrupt  = Event()
    bCachedIsBright = False

    def OnEdgeDetected1(self, channel):
        if self.OnButton1 != None:
            self.OnButton1()
        pass

    def OnEdgeDetected2(self, channel):
        if self.OnButton2 != None:
            self.OnButton2()
        pass

    def OnEdgeDetected3(self, channel):
        if self.OnButton3 != None:
            self.OnButton3()
        pass

    def OnEdgeDetected4(self, channel):
        if GPIO.input(channel) == GPIO.LOW:
            if  self.OnButton4 != None:
                self.OnButton4()
        else:
            if self.OnButton4_released != None:
                self.OnButton4_released()
        pass

    def __init__(self):
        self.pixels = neopixel.NeoPixel(
            pixel_pin, num_pixels, brightness=1.0, auto_write=False, pixel_order=ORDER
        )

        # touch input setup
        print("setting up touch input")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.PinButton4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 4
        GPIO.setup(config.PinButton3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 3
        GPIO.setup(config.PinButton1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 1
        GPIO.setup(config.PinButton2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button 2
        
        GPIO.add_event_detect(config.PinButton1, GPIO.FALLING, callback=self.OnEdgeDetected1)
        GPIO.add_event_detect(config.PinButton2, GPIO.FALLING, callback=self.OnEdgeDetected2)
        GPIO.add_event_detect(config.PinButton3, GPIO.FALLING, callback=self.OnEdgeDetected3)
        GPIO.add_event_detect(config.PinButton4, GPIO.BOTH, callback=self.OnEdgeDetected4)

        # light sensor setup
        i2c = board.I2C()
        self.lightsensor = adafruit_tsl2591.TSL2591(i2c)
        self.lightsensor.gain = adafruit_tsl2591.GAIN_HIGH
        self.lightsensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS
        # polling thread
        self.LightSensorPollingThread = threading.Thread(target=self.PollLightSensor)
        self.LightSensorPollingThread.start()

        pass

    def __del__(self):
        self.pixels.deinit()
        pass

    def Cleanup(self):
        self.PollingThreadInterrupt.set()
        self.LightSensorPollingThread.join()

    def BindCallbacks(self, callback1, callback2, callback3, callback4, callback4_rel, callbackLightlevel):
        self.OnButton1 = callback1
        self.OnButton2 = callback2
        self.OnButton3 = callback3
        self.OnButton4 = callback4
        self.OnButton4_released = callback4_rel
        self.OnLightlevelChanged = callbackLightlevel
        pass
            
    def PollLightSensor(self):
        while not self.PollingThreadInterrupt.is_set():
            time.sleep(1)
            bIsBright = self.lightsensor.visible >= config.VisibleLightThreshold
            print("Polled visible light level {0}".format(self.lightsensor.visible))
            if bIsBright != self.bCachedIsBright:
                self.bCachedIsBright = bIsBright

                # call light level change callback
                if self.OnLightlevelChanged != None:
                    self.OnLightlevelChanged()

        pass

    def SetPixel(self, coordinates = (0, 0), color = (0, 0, 0)):
        if coordinates[0] % 2 == 0:
            i = coordinates[0] * 22 + coordinates[1] * 2
        else:
            i = coordinates[0] * 22 + (10 - coordinates[1]) * 2
        self.pixels[i] = color
        self.pixels[i+1] = color
        pass

    def UpdateLEDs(self, enabledLEDs={}):
        self.pixels.fill((0, 0, 0))

        for l in enabledLEDs:
            color = enabledLEDs[l]
            self.SetPixel(l, color)
        self.pixels.show()
        pass

    def UpdateLEDs_FixedColor(self, color, enabledLEDs=[]):
        self.pixels.fill((0, 0, 0))
        
        for l in enabledLEDs:
            self.SetPixel(l, color)
        self.pixels.show()

        pass

    def GetCurrentBrightness(self):
        if self.bCachedIsBright:
            return config.BrightnessDay
        else:
            return config.BrightnessNight