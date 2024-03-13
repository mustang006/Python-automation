import keyboard
from time import sleep
import pyautogui
import os
from pynput.mouse import Controller

myMouse = Controller()

class coordinates:
    X_Coordinates = int
    Y_Coordinates = int

    def __init__(self, X_Coordinates, Y_Coordinates):
        self.X_Coordinates = X_Coordinates
        self.Y_Coordinates = Y_Coordinates

wrInputBoxcrd = coordinates(165, 969)

# wrOKButton = coordinates(876, 546)
wrOKButton = coordinates(170, 1034)

profileCoordinates = [coordinates(993, 461),coordinates(993, 482),coordinates(993, 502),coordinates(991, 525),coordinates(993, 550),coordinates(993, 567),coordinates(993, 590),coordinates(992, 541),coordinates(991, 557),coordinates(993, 579)]
profileCoordinate = coordinates(993,461)

theUpButton = coordinates(1118, 457)
theDownButton = coordinates(1119, 587)

theProfileManagerOkButton = coordinates(1004, 673)



def theMainFunction(i):
    keyboard.write("Happy teachers day")
    sleep(0.5)
    keyboard.press_and_release('Enter')
    pyautogui.click()
    sleep(0.1)




def gotoSearchBar():
    sleep(1)
    myMouse.position = (1315,1047)
    pyautogui.click()
    


    
    
    for i in range(0, 2):
        gotoSearchBar()
        theMainFunction()
        # keyboard.write("HAPPY TEACHERS DAY MAMA")
        # sleep(1.5)
        # keyboard.press_and_release('Enter')
        
    #     sleep(1)
    # turnsOnVPN()
    # sleep(1)

    
    # for k in range(0, 2):
    #     gotoSearchBar()
    #     keyboard.write(splitSente02[k])
    #     sleep(1)
    #     keyboard.press_and_release('Enter')

    
    
    
    # for j in range(0, 3):
    #     gotoSearchBar()
    #     keyboard.write(splitSente01[j])
    #     sleep(3)
    #     keyboard.press_and_release('Enter')

    
    # for k in range(0, 3):
    #     gotoSearchBar()
    #     keyboard.write(splitSente02[k])
    #     sleep(3)
    #     keyboard.press_and_release('Enter')
        
        
