states = ["Washington","Oregon","California"]

#iterating throug a list using for loop 
#for state in states:
#    state = state.upper()
#    print(state)

#check if  a keyword is in a list
print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

#concatenating list 
states2 = ['Arizona','Ohio','Louisiana']
best_states = states + states2
print(best_states)


#slicing list 
print(best_states[1:3])
print(best_states[:2])
print(best_states[4:])

#looping using range fuction
#for i in range(len(best_states)):
  #  print(best_states[i])

#looping using while loop 
n = 0 
while n < len(best_states):
    print(best_states[n])
    n = n +1

#list comprehension syntax newlist = [expression for item in iterable if condition == True]
[print(x) for x in best_states]

#create a new lsit with stetes that contains latter "o"
#with list comprehension 
#new_states =[]

#for x in best_states:
#if "a" in x:
 #       new_states.append(x)
#print(new_states)

new_states = [x.upper() for x in best_states if "a" in x]
print(new_states)

best_states.sort()
print(best_states)

best_states.sort(reverse=True)
print(best_states)