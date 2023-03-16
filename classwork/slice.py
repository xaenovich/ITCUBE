n = input()
r = 0
c = 0
for i in range(len(n)):
    m = n.count(n[i])
    if m > r:
        c = n[i]
        r = m

print(c)
