from turtle import *
i = 0

n = int(input())

while n != 1:
    if n % 2 != 0:
        n = n * 3 + 1
    if n % 2 == 0:
        n = n // 2 
        
    i += 10
    goto(i,n)
    print(n)
done()
