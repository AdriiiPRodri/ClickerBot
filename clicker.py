from pymouse import PyMouse, PyMouseEvent
import pyautogui as gui
import time
import sys

class clickerBot(PyMouseEvent):
    def __init__(self, t_clicks):
        self.mouse = PyMouse()
        gui.PAUSE = float(t_clicks)
        self.__setPositionForClick()

    def __setPositionForClick(self):
        key = 'n'
        while key != '':
            key = input()
        self.coords = self.mouse.position()
    
    def __detectKeyStroke(self):
        if self.mouse.position() != self.coords:
            return 1
        return 0

    def start(self):
        while self.__detectKeyStroke() != 1:
            gui.click(x = self.coords[0], y = self.coords[1])
    
        

def main(argv):
    print("Time beetween clicks(s):")
    t_clicks = input()
    print("Move the arrow where where you want, then press ENTER :)")
    clicky = clickerBot(t_clicks)
    clicky.start()
    print("Stopped")
        
if __name__ == "__main__":
    main(sys.argv[1:])