from turtle import *

i = 0
n = int(input())

while True:
    if n % 2 != 0:
        n = n * 3 + 1
    elif n % 2 == 0:
        n = n // 2
    print(n)
    if n == 1:
        break
        
    i += 10
    goto(i,n)
    
done()
