# Loops

array = [2, 3, 4, 5]

for num in array: # for each
    print(num)


for x in range(5):
    print("Babu Gumpu")


for x in range(5, 10):
    print(x)


print("#########");


for x in range(5, 500, 200):
    print(x)

print("#########");
count = 0
while count < 5:
    print(count);
    count += 1

print("---------------------------");
count = 0
while count < 10:
    print(count)
    count += 1
    if count >= 5:
        break

print("Print only Odd Numbers")

for x in range(20):
    if x % 2 == 0:
        print('Even Number --->', x)
    else:
        print('Odd Number --> ', x)
