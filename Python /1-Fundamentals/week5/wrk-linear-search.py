import random

def guess_random_number(tries, start, stop):
    targetnumber = random.randrange(start, stop)
    print("The number the program to guess is:", targetnumber)
    for x in range(start, stop):
        if x == targetnumber:
            print("Found it ")
            return 
        elif x > targetnumber:
            print("The program is guessing ......", x )
            tries -= 1 
            print("The number of tries left:", tries)

        elif x < targetnumber:
            print("The program is guessing ......", x )
            tries -= 1
            print("The number of tries left:", tries)
        if tries == 0:
            print("failed ")
            break
        

guess_random_number(5,0,10)