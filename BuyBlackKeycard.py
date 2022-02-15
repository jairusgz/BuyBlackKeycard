import pyautogui
import keyboard
import time

#Change if you have a different resolution than 1920x1080
WIDTH = 1920
HEIGHT = 1080

x_1 = 1750 * (WIDTH / 1920)
y_1 = 180 * (HEIGHT / 1080)

x_2 = 1000 * (WIDTH / 1920)
y_2 = 780 * (HEIGHT / 1080)

if __name__ == '__main__':
    
    time.sleep(10)
    
    while not keyboard.is_pressed('Escape'):
        pyautogui.moveTo(x_1, y_1)
        pyautogui.click()
        pyautogui.moveTo(x_2, y_2)
        pyautogui.click()
        pyautogui.press('f5')
