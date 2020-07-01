phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here

phonebook["Jake"] = 7581470833

print(phonebook)

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

del phonebook["Jill"]
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

print(phonebook)