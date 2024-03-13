import keyboard
from time import sleep
import pyautogui
import os
from pynput.mouse import Controller

myMouse = Controller()

def gotosearchbar():
    myMouse.position = (1308,1062)
    pyautogui.click();
    
for j in range(0,1):
    gotosearchbar()
    
for i in range(0,2) :
    sleep(0.5)
    myMouse.position = (1315,1047)
    
    pyautogui.click() 
    keyboard.write("Happy teachers day")
    sleep(0.5)
    keyboard.press_and_release('Enter')
    sleep(1)
  
