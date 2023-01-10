g = input('Пол(f или m) : ')
y = int (input('Возраст : '))

if g == 'f':
    if y >= 10:
        if y <= 15:
            print('YES')
else:
    print('NO')