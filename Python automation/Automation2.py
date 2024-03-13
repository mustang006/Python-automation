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
    keyboard.press_and_release('Windows + r')
    sleep(1)
    myMouse.position = (wrInputBoxcrd.X_Coordinates, wrInputBoxcrd.Y_Coordinates)
    keyboard.press_and_release('ctrl + a')
    keyboard.press_and_release('Backspace')
    sleep(0.5)
    keyboard.write("firefox.exe -P")
    sleep(0.5)
    myMouse.position = (wrOKButton.X_Coordinates, wrOKButton.Y_Coordinates)
    sleep(0.5)
    pyautogui.click()
    sleep(1)
    myMouse.position = (theUpButton.X_Coordinates, theUpButton.Y_Coordinates)
    pyautogui.click()
    sleep(0.5)
    pyautogui.click()
    sleep(1)
    myMouse.position = (profileCoordinate.X_Coordinates, profileCoordinate.Y_Coordinates)
    pyautogui.click()
    sleep(1)
    for j in range(0, i):
        keyboard.press_and_release('Down')
        sleep(0.5)
    sleep(1)
    myMouse.position = (theProfileManagerOkButton.X_Coordinates, theProfileManagerOkButton.Y_Coordinates)
    sleep(0.5)
    pyautogui.click();



def closesbrowser():
    try:
        os.system('TASKKILL /F /IM firefox.exe')
    except Exception as e:
        print(e)


def gotoSearchBar():
    myMouse.position = (962, 65)
    pyautogui.click()
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('backspace')
    pyautogui.click()

def turnsOnVPN():
    myMouse.position = (1862,62)
    sleep(0.9)
    pyautogui.click()
    
    sleep(1)

Coordinates = [coordinates(1695,537), coordinates(1671,503)]
sentence01 = "Etymology tealogy qwartz sneakers Yamada-Kun Ryu Shiraishi Toranosuke Ino Miki Yoshikawa Manga Hattori Shin-Chan Miyamura Tempura Ramen Takayoki French-Fries Sauce Italian-Cuisine Cuisines Dragons Mermaids Unicorns Pegasus Wings KFC java yezdi"
splitSente01 = sentence01.split()
sentence02 = "dart-frogs blue-ringed-octopus Cardio Morphology Molting Insomnia Visa License Equador Bulldogs axolotl brownies chimpanzee Builders Iron-Man Istanbul Capitals Devonshire Milky-Way Galaxies Rocket-Thrusters Bulldozers bughatti vaseline jello albatros dwarfs trolls boxtrolls obnoxius"
splitSente02 = sentence02.split()

for i in range(0, 11):
    theMainFunction(i)
    sleep(2)
    
    
    for j in range(0, 30):
        gotoSearchBar()
        keyboard.write(splitSente01[j])
        sleep(1.5)
        keyboard.press_and_release('Enter')
        
        sleep(1)
    turnsOnVPN()
    sleep(1)

    
    for k in range(0, 30):
        gotoSearchBar()
        keyboard.write(splitSente02[k])
        sleep(1)
        keyboard.press_and_release('Enter')

    
    
    
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
        
        sleep(1)
    turnsOnVPN()
    sleep(1)
        
    closesbrowser()
    sleep(2)
