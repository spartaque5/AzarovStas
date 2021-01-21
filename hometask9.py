import random

a = [random.randint(0, 99) for i in range(10)]
b = [random.randint(0, 99) for o in range(10)]
result = list(set(a + b))
print(result)
