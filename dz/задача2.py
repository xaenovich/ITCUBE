count = 0 
maximum = 0
for i in range(8):
    x = int(input())
    if x % 4 == 0 and -10**12 <= x < 10**12:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')