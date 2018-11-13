import platform
import pyautogui as gui
import numpy as np
import sys
import time

if platform.system() == 'Linux':
    import pyscreenshot as ImageGrab
    from PIL import ImageOps
else:
    from PIL import ImageGrab, ImageOps

class botDinosaur:
    def __init__(self):
        self.replayBtn = (180, 600)
        self.topRightDino = (255, 379)
        self.xDistanceToObstacleCloser = 325  # Diferencia aplicada
        self.yDistanceToObstacleCloser = 369  # Diferencia aplicada
        self.xDistanceToObstacle = 378  # Diferencia aplicada
        self.yDistanceToObstacle = 404  # Diferencia aplicada

    def restartGame(self):
        gui.click(x = self.replayBtn[0], y = self.replayBtn[1])

    def dinoJump(self):
        gui.keyDown(key = 'space')
        gui.keyUp(key = 'space')

    def obstacleDetection(self):
        bbox = (self.xDistanceToObstacleCloser, 
                self.yDistanceToObstacleCloser,
                self.xDistanceToObstacle,
                self.yDistanceToObstacle)

        anilizeRGB = ImageGrab.grab(bbox = bbox)
        analizeGray = ImageOps.grayscale(anilizeRGB) # Analysing images in grayscale is more effecient than in RGB
        grey_array = np.array(analizeGray.getcolors()) # Check if the sum of pixel is grey or not
        return grey_array.sum()

def main(argv):
    gui.PAUSE = 0.02
    dino = botDinosaur()
    contador = 0
    while(1):
        contador += 1
        dino.restartGame()
        if contador == 700:
            time.sleep(5)
            contador = 0
        
if __name__ == "__main__":
    main(sys.argv[1:])