# Dictionary
phonebook = {}

phonebook["Babu"] = 7581470833
phonebook["Shilpa"] = 7794487128

print(phonebook)

# Iterating Over Dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is -->%s" % (name, number))

phonebook2 = {
    "A": 123456,
    "B": 234567,
    "C": 345678
}

print(phonebook2)
print(phonebook)

del phonebook["Babu"]

print(phonebook)
print(phonebook.pop("Shilpa"))
print(phonebook.keys())
print(phonebook)


