line = input('Введите строку содержащую букву f')

for _ in range(len(line)):
    counter = line.count('f')
    index = line.find('f')

    if counter > 1:
        reverse = line[::-1]
        find = reverse.find('f') + 1
        index2 = len(line) - find 


if counter == 1:
    print('Единственный индекс: 'index)
elif counter > 1:
    print('Первый: 'index,'Последний: 'index2)
else:
    print('NO')
