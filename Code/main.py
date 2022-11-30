import sys
import time
from threading import Event

if sys.platform.startswith("win"):
    import LEDcontrolWindows as LEDcontrol
else:
    import LEDcontrolRaspi as LEDcontrol
import HelperFunctionLibrary as FuncLib
import config

print("Platform:", sys.platform)

LEDcontroller = LEDcontrol.controller()

# https://stackoverflow.com/questions/5114292/break-interrupt-a-time-sleep-in-python
InputInterrupt = Event()
ExitInterrupt = Event()
ButtonHoldInterrupt = Event()
TestingInterrupt = Event()
SecondsInterrupt = Event()
LogoInterrupt = Event()
CustomInterrupt = Event()

def GetColorWithBrightness(color):
    b = LEDcontroller.GetCurrentBrightness()
    return (int(color[0]*b), int(color[1]*b), int(color[2]*b))

def TestDisplay():
    c = (230, 60, 25)
    for h in range(12):
        LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetCoordinatesForTime(h, 0))
        if InputInterrupt.wait(1):
            TestingInterrupt.clear()
            return

    for h in range(12):
        LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetCoordinatesForTime(h, 10))
        if InputInterrupt.wait(1):
            TestingInterrupt.clear()
            return

    for m in range(60):
        LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetCoordinatesForTime(0, m))
        if InputInterrupt.wait(1):
            TestingInterrupt.clear()
            return
    
    for i in range(60):
        LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetCoordinatesForSeconds(i))
        if InputInterrupt.wait(0.5):
            TestingInterrupt.clear()
            return

    TestingInterrupt.clear()

def DisplayRainbow(coordinates = [], activationDelay = 0.1, cyclespeed = 100, cyclelength = 10, displayTimeOffset = 3):
    starttime = time.time()
    passedTime = 0
    
    while passedTime < len(coordinates) * activationDelay + displayTimeOffset:
        passedTime = time.time() - starttime

        leds = {}

        for i in range(len(coordinates)):
            if passedTime >= i * activationDelay:
                leds[coordinates[i]] = GetColorWithBrightness(FuncLib.GetRainbowColor(i * 768 / cyclelength + passedTime * cyclespeed))

        LEDcontroller.UpdateLEDs(leds)
        # using CustomInterrupt instead of InputInterrupt.wait() since the wait time during this anim is very short so there's a good chance the interrupt is set and cleared while LEDs are updated and thus the function wouldn't be interrupted
        if CustomInterrupt.is_set(): 
            CustomInterrupt.clear()
            return
        # if InputInterrupt.wait(0.01):
            # return

def DisplayLogoAnimation():
    print("Displaying logo animation")
    CustomInterrupt.clear()
    DisplayRainbow(FuncLib.GetSpiralCoordinates(), activationDelay = 0.05, cyclespeed=-100, cyclelength=100, displayTimeOffset=0)
    DisplayRainbow(FuncLib.GetWatermarkCoordinates(), activationDelay=0, cyclespeed=100, cyclelength=13, displayTimeOffset=5)
    LogoInterrupt.clear()

def DisplayTime():
    print("Displaying time")

    currentTime = time.localtime()

    if currentTime.tm_hour >= 11:
        c = GetColorWithBrightness(config.ColorPM)
    else:
        c = GetColorWithBrightness(config.ColorAM)

    LEDcontroller.UpdateLEDs_FixedColor(
        c, FuncLib.GetCoordinatesForTime(currentTime.tm_hour, currentTime.tm_min))
    # LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetCoordinatesForTime(18, 42))
    InputInterrupt.wait(60 - currentTime.tm_sec)


def DisplaySeconds():
    print("Displaying current seconds")
    c = GetColorWithBrightness(config.ColorSeconds)

    for _ in range(10):
        LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetCoordinatesForSeconds(time.localtime().tm_sec))
        if InputInterrupt.wait(1 - time.time() % 1):
            SecondsInterrupt.clear()
            break

        
    SecondsInterrupt.clear()

def DisplayExitAnimation(waitTime = 1):
    c = GetColorWithBrightness((255, 255, 255))
    for i in range(5):
        LEDcontroller.UpdateLEDs_FixedColor(c, FuncLib.GetDotCoordinates(i))
        if ButtonHoldInterrupt.wait(waitTime):
            print("Hold interrupted")
            ExitInterrupt.clear()
            return False
    return True

def OnButton1Pressed():
    print("Button1 was pressed")
    InputInterrupt.set()
    CustomInterrupt.set()
    InputInterrupt.clear()
    SecondsInterrupt.set()


def OnButton2Pressed():
    print("Button2 was pressed")
    InputInterrupt.set()
    CustomInterrupt.set()
    InputInterrupt.clear()
    LogoInterrupt.set()


def OnButton3Pressed():
    print("Button3 was pressed")
    InputInterrupt.set()
    CustomInterrupt.set()
    InputInterrupt.clear()
    TestingInterrupt.set()


def OnButton4Pressed():
    print("Button4 pressed")
    InputInterrupt.set()
    CustomInterrupt.set()
    InputInterrupt.clear()
    ExitInterrupt.set()

def OnButton4Released():
    print("Button 4 released")
    ButtonHoldInterrupt.set()
    ButtonHoldInterrupt.clear()

def OnLightlevelChanged():
    print("Lightlevel change detected")
    InputInterrupt.set()
    InputInterrupt.clear()


LEDcontroller.BindCallbacks(
    OnButton1Pressed, OnButton2Pressed, OnButton3Pressed, OnButton4Pressed, OnButton4Released, OnLightlevelChanged)

DisplayLogoAnimation()

bProgramActive = True
while bProgramActive:
    if ExitInterrupt.is_set():
        if DisplayExitAnimation(waitTime=0.2):
            print("Exiting program..")
            LEDcontroller.UpdateLEDs()
            break
    elif SecondsInterrupt.is_set():
        DisplaySeconds()
    elif LogoInterrupt.is_set():
        DisplayLogoAnimation()
    elif TestingInterrupt.is_set():
        TestDisplay()
    elif not InputInterrupt.is_set():
        DisplayTime()


InputInterrupt.clear()

# stop when clicking with mouse inside the window
if sys.platform.startswith("win"):
    LEDcontroller.win.getMouse()

del LEDcontroller