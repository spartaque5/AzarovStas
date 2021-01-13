a = 0
b = 1000
c = 250
while a != b:
    if a <= b:
        print('a =', a, '< b =', b)
    a += c
else:
    print("Пока еще нет a =", a, ',b =', b)
a = 0
b = 100
c = 25
while a <= b:
    print('a =', a, '< b =', b)
    a += c
else:
    print('Наканец a =', a, '> b =', b)
