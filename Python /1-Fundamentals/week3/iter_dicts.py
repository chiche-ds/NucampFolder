state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}


""" for states in state_capitals:
    print(states) """

for city in state_capitals.values():
    print(city)

#iterate both keys and values 
"""for state in state_capitals:
    print(state_capitals[state], "is the capital of ", state)"""

for state, city in state_capitals.items():
    print(city, "is the capital of ", state)