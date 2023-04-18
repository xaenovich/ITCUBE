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
    
while True:
    far,frame = cap.read()
    hsv = cvtColor(frame,COLOR_BGR2HSV)
    
    #Подбор рандомных цветов
    while counter != 3:
        item = all_colors[randint(0,2)]
        if last_color != item:
            rand_colors.append(item)
            last_color = item
            counter += 1
        
    for color_name,(lower,upper) in colors.items():
        mask = inRange(hsv,lower,upper)
        count = countNonZero(mask)
        if count > 10000: #Проверка количества пикселей не равных 0
            putText(frame,color_name,(100,100),FONT_HERSHEY_TRIPLEX,1,(155,0,155),2) #Вывод на экран название цвета
            if last_color != color_name:
                color_lst.append(color_name)
                last_color = color_name
            break

    imshow('stream',frame)

    #Выключение по нажатию или если набрано достаточно цветов
    if waitKey(1) == ord('q') or len(color_lst) == 3:
        break

destroyAllWindows()
print(color_lst)
print(rand_colors)

#Сравнение показаных и рандомных цветов
if color_lst == rand_colors:
    print('Вы выйграли!')
