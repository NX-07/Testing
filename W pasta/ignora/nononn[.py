import os
from time import sleep
import pyautogui

pyautogui.moveTo(750, 730, duration=1)
sleep(2)
pyautogui.click()
sleep(2)
pyautogui.moveTo(260, 375, duration=1)
sleep(2)
pyautogui.click()
pyautogui.moveTo(300, 375, duration=1)
sleep(2)
pyautogui.click()
sleep(1)
pyautogui.click(button='right')
sleep(1)
pyautogui.moveTo(310, 270, duration=1)
sleep(2)
pyautogui.click()
sleep(1)
pyautogui.moveTo(800, 490, duration=1)
sleep(2)
pyautogui.click()
pyautogui.click()
sleep(1)
pyautogui.moveTo(310, 268, duration=1)
sleep(2)
pyautogui.click()
sleep(1)
pyautogui.doubleClick()
sleep(2)
pyautogui.write("W escrita")


def clear():
    os.system("cls")


clear()
print("\033[0;31;40mW letra\033[m")