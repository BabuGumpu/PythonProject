
response = ""
while response != "Because. ":
    response = input("why? \n")

print("Oh Ok")

print("Press Enter to Exit")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls = 0
    health -= damage
    print(health, "----", damage)