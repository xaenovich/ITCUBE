line = input()

for _ in range(len(line)):
    counter = line.count('h')
    index = line.find('h')

    if counter >= 2:
        reverse = line[::-1]
        find = reverse.find('h')
        index2 = len(line) - find
        
print(line[:index],line[index2:],sep = '')
