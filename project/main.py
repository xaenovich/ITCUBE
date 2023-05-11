from cv2 import waitKey,VideoCapture,cvtColor,inRange,countNonZero,putText,imshow,destroyAllWindows,FONT_HERSHEY_TRIPLEX,COLOR_BGR2HSV
from numpy import array
from random import randint

all_colors = ['red','green','blue']
color_lst = []
rand_colors =[]
last_color = ''
counter = 0

#Границы Красного
lower_r = array([170,100,90])
upper_r = array([255,255,255])

#Границы Зеленого
lower_g = array([50,20,120])
upper_g = array([90,120,255])

#Границы Синего
lower_b = array([95,70,140])
upper_b = array([105,255,255])

colors = {
    'red' : [lower_r,upper_r],
    'green' : [lower_g,upper_g],
    'blue' : [lower_b,upper_b],
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
        if count > 50000:
            putText(frame,color_name,(100,100),FONT_HERSHEY_TRIPLEX,1,(155,0,155),2)
            if last_color != color_name:
                color_lst.append(color_name)
                last_color = color_name
            break

    imshow('stream',frame)
    if waitKey(1) == ord('q') or color_lst == rand_colors:
        break
    elif len(color_lst) == 3 and color_lst != rand_colors:
        color_lst = []
    #Выключение по нажатию или если набрано достаточно цвето
destroyAllWindows()
print(color_lst)
if color_lst == rand_colors:
    print('Вы выйграли')
