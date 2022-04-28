import pyautogui
from time import sleep
import winsound

def findPosition(second):
    sleep(0.5)
    for i in range(0,second):
        winsound.Beep(500,250)
        sleep(0.750)
    X,Y = pyautogui.position()
    winsound.Beep(250,750)
    return X,Y


