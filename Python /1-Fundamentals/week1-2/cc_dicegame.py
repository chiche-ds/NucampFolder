import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("current High Score:", high_score)
        print("1)   Roll Dice")
        print("2)   Leave Game")
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            score1 = random.randint(1, 6)
            print("you roll a ...", score1)
            score2 = random.randint(1,6)
            print("You roll a ...", score2)
            total_score = score1 + score2
            if total_score > high_score:
                high_score = total_score
                print("New high score!")
        elif choice == 2:
            print("Goodbye!")
            break


dice_game()
