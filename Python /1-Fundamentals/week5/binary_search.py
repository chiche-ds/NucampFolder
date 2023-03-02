""" def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
    return -1


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
print(binary_search(test_list, 4))
print(binary_search(test_list, 33)) """

import random
 

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
