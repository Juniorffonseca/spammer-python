import random
import pyautogui as pg
import time
words = ('bro', 'man', 'dude')
time.sleep(8)

for i in range(100):
    a = random.choice(words)
    pg.write('what r u making' + a)
    pg.press('enter')
