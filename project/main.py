from cv2 import waitKey,VideoCapture,cvtColor,inRange,countNonZero,putText,imshow,destroyAllWindows,FONT_HERSHEY_TRIPLEX,COLOR_BGR2HSV
from numpy import array
from random import randint

all_colors = ['red','green','blue']
color_lst = []
rand_colors =[]
last_color = ''
counter = 0

# Цвета и их границы
colors = {
    'red' : [array([170,100,90]),array([255,255,255])],
    'green' : [array([50,20,120]),array([90,120,255])],
    'blue' : [array([95,70,140]),array([105,255,255])],
}

cap = VideoCapture(0)

while counter != 3:
    item = all_colors[randint(0,2)]
    if last_color != item:
        rand_colors.append(item)
        last_color = item
        counter += 1

print(rand_colors)

while True:
    far,frame = cap.read()
    hsv = cvtColor(frame,COLOR_BGR2HSV)  
    for color_name,(lower,upper) in colors.items():
        mask = inRange(hsv,lower,upper)
        count = countNonZero(mask)
        if count > 100000:
            putText(frame,color_name,(100,100),FONT_HERSHEY_TRIPLEX,1,(155,0,155),2)
            if last_color != color_name:
                color_lst.append(color_name)
                last_color = color_name
            break

    imshow('stream',frame)

    if waitKey(1) == ord('q') or color_lst == rand_colors:
        print(color_lst)
        break
    elif len(color_lst) == 3 and rand_colors != color_lst:
        color_lst = []

destroyAllWindows()

if color_lst == rand_colors:
    print('Вы выйграли')
