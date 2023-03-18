line = input()

for _ in range(len(line)):
    counter = line.count('f')
    index = line.find('f')

    if counter > 1:
        reverse = line[::-1]
        find = reverse.find('f') + 1
        index2 = len(line) - find 


if counter == 1:
    print(index)
elif counter > 1:
    print(index,index2)
else:
    print('NO')