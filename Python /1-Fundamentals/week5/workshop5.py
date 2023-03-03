import random
def guess_random_number(tries,start,stop):
    target_num = random.randrange(start, stop + 1)
    while tries != 0:
        print(tries)
        n = "guess a number between " 
        num_guess = int(input("guess a number: " ))
        if num_guess == target_num:
            print("success")
            return
        elif num_guess > target_num:
            print("guess lower")
            tries -= 1
        elif num_guess < target_num:
            print("guess higher")
            tries -= 1
        if tries == 0:
            print("you failed ")
            break


guess_random_number(5,1,15)
#task 2 linear search 
def guess_random_number(tries, start, stop):
    targetnumber = random.randrange(start, stop)
    print("The number the program to guess is:", targetnumber)
    for x in range(start, stop):
        if x == targetnumber:
            print("Found it ...")
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
#Task 3 binarry search 
def guess_random_num_binary(tries, start, stop):
    target_number = random.randrange(start, stop )
    list = range(start, stop )
    left = 0
    right = len(list) - 1
    print("Random number to find ", target_number)
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target_number:
            print("Found it !", mid)
            return
        elif target_number < list[mid]:
            print("Guess higher !")
            right = mid -1 
            tries -= 1
        else:
            print("Guess lower !")
            left = mid + 1 
            tries -= 1
        if tries == 0:
            print("Your Program Failed")
            break
    return - 1 

guess_random_num_binary(5,0,100)
