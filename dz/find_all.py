def find_all(target,symbol):
    lst = []
    while symbol in target:
        x = target.find(symbol)
        lst.append(x)
        target = target[:x] + target[x + 1:]
    return lst

text = input()
symbol = input()
print(find_all(text,symbol))
