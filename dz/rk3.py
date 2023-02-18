s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0 and -10**6 <= n <= 10**6:
        s += n
print(s)
