a = 3
b = 6


def spremeni():
    global a, b
    a += 1
    b += 1


print(a, b)
spremeni()
print(a, b)
