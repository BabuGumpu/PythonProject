#Craps Roller
# Demonstrates Random Number Generations
import random

die1 = random.randint(10,60)
die2 = random.randrange(100)
total = die1 + die2

print("You have rolled a", die1, "and a", die2, "for a total of -- ", total)
