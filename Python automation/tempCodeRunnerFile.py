from pynput.mouse import Controller
from time import sleep

myMouse = Controller()

print("Prints all coordinates of profiles ")
sleep(5)
print(myMouse.position)