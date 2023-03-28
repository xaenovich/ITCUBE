n = int(input())
print(n + (n % 2 == 0) * 10 - (n % 2 != 0) * 10)
