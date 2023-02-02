from math import ceil
i = 0

while i == 0:
    i = float(input())
    i = ceil(i)
    
    if i >= 10.25:
         i = i // 10.25 
         
    if i >= 1.5:
        i = i // 1.5
        
print (i)
