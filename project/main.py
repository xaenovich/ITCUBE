import cv2 as cv
import numpy as np
from random import randint

all_colors = ['red','green','blue']
color_lst = []
rand_colors =[]
last_color = ''
counter = 0

lower_r = np.array([170,100,90])
upper_r = np.array([255,255,255])

lower_g = np.array([50,20,120])
upper_g = np.array([90,120,255])

lower_b = np.array([95,70,140])
upper_b = np.array([105,255,255])

colors = {
    'red' : [lower_r,upper_r],
    'green' : [lower_g,upper_g],
    'blue' : [lower_b,upper_b],
}

cap = cv.VideoCapture(1)
    
while True:
    far,frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    while counter != 3:
        item = all_colors[randint(0,2)]
        if last_color != item:
            rand_colors.append(item)
            last_color = item
            counter += 1
        
    for color_name,(lower,upper)in colors.items():
        mask = cv.inRange(hsv,lower,upper)
        count = cv.countNonZero(mask)
        if count > 1000:
            cv.putText(frame,color_name,(100,100),cv.FONT_HERSHEY_TRIPLEX,1,(155,0,155),2)
            if last_color != color_name:
                color_lst.append(color_name)
                last_color = color_name
            break

    cv.imshow('streem',frame)

    if cv.waitKey(1) == ord('q') or len(color_lst) == 3:
            break

cv.destroyAllWindows()
print(color_lst)
print(rand_colors)
if color_lst == rand_colors:
    print('Вы выйграли!')
