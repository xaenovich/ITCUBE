one = 0
two = 0
three = 0
four = 0

for i in range(int(input())):
    n = input().split()
    if int(n[0]) > 0 and int(n[1]) > 0:
        one += 1
    elif int(n[0]) < 0 and int(n[1]) > 0:
        two += 1
    elif int(n[0]) < 0 and int(n[1]) < 0:
        three += 1
    elif int(n[0]) > 0 and int(n[1]) < 0:
        three += 1
print(one, two, three, four, sep = '\n')
