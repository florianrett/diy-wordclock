from graphics import GraphWin, Text, Point, Circle, color_rgb
import time
import keyboard
import config

class controller:

    win = None

    OnButton1 = None
    OnButton2 = None
    OnButton3 = None
    OnButton4 = None
    OnButton4_released = None
    Button4Down = False
    OnLightlevelChanged = None

    currentLightlevel = 0
    lastLightlevelChange = 0

    LEDs = {}

    def __OnKey1(self, arg):
        if self.OnButton1 != None:
            self.OnButton1()

    def __OnKey2(self, arg):
        if self.OnButton2 != None:
            self.OnButton2()

    def __OnKey3(self, arg):
        if self.OnButton3 != None:
            self.OnButton3()

    def __OnKey4(self, arg):
        # print("Callback", arg.event_type == "down")
        # keyboard.KeyboardEvent.event_type
        if arg.event_type == "down":  
            if self.Button4Down == False:
                self.Button4Down = True
                if self.OnButton4 != None:
                    self.OnButton4()
        else:
            self.Button4Down = False
            if self.OnButton4_released != None:
                self.OnButton4_released()

    def __OnKeyL(self, arg):
        if time.time() - self.lastLightlevelChange >= 1:
            self.lastLightlevelChange = time.time()
        else:
            return

        self.currentLightlevel +=  1
        self.currentLightlevel %= 2

        if self.OnLightlevelChanged != None:
            self.OnLightlevelChanged()

    def __init__(self):
        self.win = GraphWin("WordClock", 600, 600)

        letters = ["ESVISTKFÜNF", "ZEHNMADEVOR", "DREIVIERTEL", "JNACHBYHALB", "ACHTDREIELF",
                   "ZWEIFLOFÜNF", "SECHSPZEHNX", "VIERRETTEIN", "ZWÖLFSIEBEN", "NEUNEINSUHR"]

        for i in range(10):
            for j in range(11):
                c = Text(Point(50+50*j, 50 + 50 * i), letters[i][j])
                c.setSize(30)
                c.setFill("black")
                c.draw(self.win)
                self.LEDs[(i, j)] = c

        for i in range(4):
            c = Circle(Point(225 + 50*i, 550), 10)
            c.draw(self.win)
            c.setFill("black")
            self.LEDs[(10, i)] = c

        keyboard.on_press_key("1", self.__OnKey1)
        keyboard.on_press_key("2", self.__OnKey2)
        keyboard.on_press_key("3", self.__OnKey3)
        keyboard.on_press_key("4", self.__OnKey4)
        keyboard.on_release_key("4", self.__OnKey4)
        keyboard.on_press_key("L", self.__OnKeyL)

    def __del__(self):
        self.win.close()

    def BindCallbacks(self, callback1, callback2, callback3, callback4, callback4_rel, callbackLightlevel):
        self.OnButton1 = callback1
        self.OnButton2 = callback2
        self.OnButton3 = callback3
        self.OnButton4 = callback4
        self.OnButton4_released = callback4_rel
        self.OnLightlevelChanged = callbackLightlevel

    # Example callback call
    # def Update(self):
    #     print(self.OnButton1)
    #     if self.OnButton1 != None:
    #         self.OnButton1()

    def UpdateLEDs(self, enabledLEDs={}):
        for l in [x for x in self.LEDs if x not in enabledLEDs]:
            self.LEDs[l].setFill("black")
            
        for l in enabledLEDs:
            color = enabledLEDs[l]
            if l in self.LEDs:
                self.LEDs[l].setFill(color_rgb(color[0], color[1], color[2]))

    def UpdateLEDs_FixedColor(self, color, enabledLEDs=[]):
        for l in [x for x in self.LEDs if x not in enabledLEDs]:
            self.LEDs[l].setFill("black")

        c = color_rgb(color[0], color[1], color[2])
        for l in enabledLEDs:
            if l in self.LEDs:
                self.LEDs[l].setFill(c)

    def GetCurrentBrightness(self):
        if self.currentLightlevel == 0:
            return 1.0
        else:
            return 0.5

# leds = controller()
# leds.win.getMouse()

# def main():
#     win = GraphWin("My Circle", 1000, 100)
#     c = Circle(Point(50,50), 10)
#     c.draw(win)
#     win.getMouse() # Pause to view result
#     win.close()    # Close window when done

# main()
