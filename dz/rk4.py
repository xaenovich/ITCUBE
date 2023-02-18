n = int(input())

digit = n // 10
max_digit = n % 10
    
if digit % 3 == 0 or max_digit % 3 == 0:
    if digit > max_digit:
        max_digit = digit
else:
    max_digit = 0
        
if max_digit == 0:
    print('NO')
else:
    print(max_digit)