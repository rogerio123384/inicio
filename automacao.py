import pyautogui
from time import sleep

pyautogui.PAUSE = 0.3

pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('kbenter')
sleep(5)
for i in range(30):
    pyautogui.press('tab')
pyautogui.write('https://www.alura.com.br')
    https://www.alura.com.br
