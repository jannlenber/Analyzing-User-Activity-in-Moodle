import pyautogui
import shutil
import time

a = 0
while a<=200:
    image = pyautogui.screenshot()
    image.save(r"C:\Users\JL FRANCISCO\Desktop\New folder\new"+str(a)+".png")
    a+=1
    time.sleep(0.5)


