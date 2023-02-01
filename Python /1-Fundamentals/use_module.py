from my_module import greet, flavor, person1
import platform

greet("Albert Einstein")
print("My favorite ice cream Flavor is ",flavor)

a = person1["age"]
print(a)


x = platform.system()
print(x)

y = dir(platform)
print(y)