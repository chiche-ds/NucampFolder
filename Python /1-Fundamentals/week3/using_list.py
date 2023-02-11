states = ["Washington","Oregon","California"]
print(states[-1])
print(states[-2])
print(states[-3])

print(states[0])
print(states[1])
print(states[2])

states[2] = "Arizona"

print(states)
#length of a list
print(len(states))
#list methods 
states.append("New York")
print(states)

states.pop()
print(states)

states.pop(1)
print(states)