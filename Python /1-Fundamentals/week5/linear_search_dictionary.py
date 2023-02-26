def linear_search_dictionary(a_dic, target):
    for x in a_dic:
        if a_dic[x] == target:
            print("Found key at ", x)
            return x
    print("Target not found")



a_dic = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(a_dic, 5)
linear_search_dictionary(a_dic, 3)
linear_search_dictionary(a_dic, 8)