my_string = "alpha"
multiline_string = """ bravo 
charlie"""

print(my_string)
print(multiline_string)

#using bracket notation to retrieve characters by index 

print(my_string[0])
print(my_string[3])

#accessing and slice characters 
print(my_string[0:3])
print(my_string[:2])
print(my_string[2:])
print(my_string)

#iterate through a string using for ... in 

for char in my_string:
    print(char)
#check if a sub string is present in a string 
print("pha" in my_string)
print("z" not in my_string)