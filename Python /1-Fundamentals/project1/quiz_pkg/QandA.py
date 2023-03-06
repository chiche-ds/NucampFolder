import random

quiz = {
        "What is the largest country in Africa by land area?": "Algeria",
        "What is the largest country in Africa by population?": "Nigeria",
        "What is the capital of Egypt?": "Cairo",
        "What is the currency of South Africa?": "South African Rand",
        "What is the name of the river that runs through the Congo rainforest?": "Congo River",
        "What is the highest mountain in Africa?": "Mount Kilimanjaro",
        "Which country in Africa was formerly known as Abyssinia?": "Ethiopia",
        "What is the name of the world's largest desert, which covers much of North Africa?": "Sahara",
        "Which African country was the first to gain independence from European colonial powers?": "Liberia",
        "What is the name of the waterfall on the Zambezi River between Zambia and Zimbabwe?": "Victoria Falls",
        "Which African country is known as the 'Rainbow Nation'?": "South Africa",
        "Which African country is known as the 'Land of a Thousand Hills'?": "Rwanda",
        "Which African country is known as the 'Giant of Africa'?": "Nigeria",
        "What is the name of the conflict in Sudan that began in 2003?": "Darfur conflict",
        "Who was the first president of Zimbabwe?": "Robert Mugabe",
        "What is the name of the current president of South Africa?": "Cyril Ramaphosa",
        "Which country is the second-largest oil producer in Africa, after Nigeria?": "Angola",
        "What is the name of the terrorist group that operates in Nigeria and neighboring countries?": "Boko Haram",
        "What is the name of the terrorist group that operates in Somalia and neighboring countries?": "Al-Shabaab",
        "Which African country is the only one that speaks Spanish as its official language?": "Equatorial Guinea",
        "What is the name of the African Union's development agency?": "NEPAD",
        "What is the name of the largest lake in Africa?": "Lake Victoria",
        "What is the name of the mountain range that runs through Morocco, Algeria, and Tunisia?": "Atlas Mountains",
        "What is the name of the animal that is commonly referred to as the 'king of the jungle' but actually lives in the savannah?": "Lion",
        "Which country is known for its coffee production and is sometimes referred to as the 'birthplace of coffee'?": "Ethiopia",
        "What is the name of the famous rock-hewn churches in Ethiopia?": "Lalibela",
        "What is the name of the coastal city in Morocco that is known for its blue-painted buildings?": "Chefchaouen",
        "Which country in Africa is the largest producer of gold?": "South Africa",
        "What is the name of the group of islands off the coast of East Africa that includes Zanzibar and Pemba?": "Zanzibar Archipelago",
        "Which country in Africa has the largest economy?": "Nigeria",
        "What is the name of the river that forms the border between Zambia and Zimbabwe?": "Zambezi River",
        "Which African country is home to the city of Timbuktu?": "Mali",
        "What is the name of the national park in Tanzania that is known for the Great Migration of wildebeest and zebras?": "Serengeti National Park",
        "What is the name of the African country that recently launched its first satellite into space, with the aim of improving weather forecasting and disaster management?": "Kenya",
    }

""" health = 5 
def logic():
    global health
    for question  in quiz:
        print(question)
        answer = input("Answer: ") 
    
        if  answer.capitalize() == quiz[question].capitalize():
            print("your great ")
            health += 1
        else:
            print("wrong")
            print("the correct answer is ",quiz[question])
            health -= 1
        if health == 0:
            print("you lose try again ")
            break
     """

def logic():
    health = 5
    while health != 0:
        random_el = random.choice(list(quiz.keys()))
        print(random_el)
        response = input("Answer: ")
        if response.upper() == quiz[random_el].upper():
            print("Correct")
            health += 1
            print("you have ", health , "lives left ")
        else:
            print("Wrong")
            print("the correct answer is ", quiz[random_el])
            health -= 1 
            print("You have ",health, " lives left ")

        if health == 10:
            print("you win ")
            break 
    print("you lose  try again ")