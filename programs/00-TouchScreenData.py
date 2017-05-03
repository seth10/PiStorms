import time, itertools, csv
import numpy as np
from PiStorms import PiStorms

psm = PiStorms()
s = psm.screen

w = s.screenWidth()
h = s.screenHeight()

x = np.linspace(0, w, 7)[1:-1].astype(int)
y = np.linspace(0, h, 7)[1:-1].astype(int)

s.termGotoLine(9) # last line, bottom of screen

data = []

for x, y in itertools.product(x, y):
    s.fillRect(x, y, 1, 1)
    
    psm.resetKeyPressCount()
    while psm.getKeyPressCount() < 1: time.sleep(0.1)
    
    i = 0
    psm.resetKeyPressCount()
    while psm.getKeyPressCount() < 1:
        data.append([x, y, s.RAW_X(), s.RAW_Y()])
        s.termReplaceLastLine('Recording %s' % i)
        i = i+1
    s.termReplaceLastLine('Stopped')

with open('/home/pi/TouchScreenData.csv', 'w') as f:
    csv.writer(f).writerows(data)

