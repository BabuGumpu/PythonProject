# Demonstrates Random Number Generation

import random

a = random.randint(1, 4)
b = random.randrange(10)

print(a)
print(b)

if a == 1:
    print("Value is one")
elif a == 2:
    print("value is Two")
elif a == 3:
    print("Value is Three")

while a != 4:
    print("While Loop Testing -->", a)
    a += 1