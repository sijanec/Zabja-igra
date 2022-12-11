a = 3
b = 6


def spremeni():
    global a, b
    a += 1
    b += 1


print(a, b)
spremeni()
print(a, b)


slovar = {"konj": 3, "kralj": 2, "dama": 3, "lovec": 3, "trdnjava": 4}


print(slovar)
abc = []
abc.append(slovar)
abc.append(slovar)
print(slovar["dama"])
slovar["dama"] -= 1
print(slovar["dama"])
print(slovar.get("slon", "Tega sploh ni v slovarju!!"))

for i, j in slovar.items():
    print(i, j)

for i in slovar:
    print(i, slovar[i])

print(abc)
