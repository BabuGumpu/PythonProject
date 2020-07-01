
myString = 'hello'
myFloat = 100.123
myInt = 222

if myString == "hello":
    print("User Input is --> Hello")
elif isinstance(myFloat, float):
    print("User input is a float")
elif isinstance(myInt, int):
    print("User Input is --> Integert")

string = "My Name is Babu Gumpu"

print("String Length -->", string.count('M'))

print("Slice 01 --->", string[3:10])
print("Slice 02 --->", string[3:10:1])
print("Slice 03 --->", string[::2])

# [start:stop:step]
