import random

# print(help(random))

options = ("rock", "paper", "sizers")
cards = ["3","4","5","6","7","8","9"]

# print(random.randint(1,6))
# between 0 and 1
# print(random.random())
# print(random.choice(options))

# random.shuffle(cards)
# print(cards)

player_input = input("write your iput")

while player_input not in options:
    print(f"options does not include {player_input}") 
    player_input = input("write your iput")
