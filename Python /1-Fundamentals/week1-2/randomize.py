import random

pips = random.randint(1, 6)
print("You roll the die... it lands with", pips, "pips showing.")

prizes = ["a car", "$1000", "a pony", "$50000"]
prize_won = random.choice(prizes)
print("You spin the wheel of fortune... it lands on a prize of ", prize_won + "!!")

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
random.shuffle(card)
print(card)