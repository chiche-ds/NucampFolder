import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]


hand = []

while diamonds:
    prompt = input("Press enter to pick a card or Q to quit:")
    if prompt == "Q" or prompt == "q":
       break
    else:
        random_index = (random.randint(0,len(diamonds)- 1))
        #a = diamonds.pop(random_index)
        hand.append(diamonds.pop(random_index))
        print("Your Hand ", hand)
        print("Remaining Cards",diamonds)

  
if not diamonds:
    print("There are no more cards to pick.")




