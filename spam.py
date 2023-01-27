import random
import pyautogui as pg
import time
words = ('aditivo a', 'aditivo b', 'aditivo c')
time.sleep(3)

for i in range(15):
    a = random.choice(words)
    pg.write('frase' + a)
    pg.press('enter')
