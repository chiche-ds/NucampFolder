def login(database,username,password):
    if username in database:
        if password == database[username]:
            print("Welcome back", username)
            return username
        print("Incorrect Password for ", username)
        return ""
    print("User not found. Please register ")
    return ""



def register(database,username):
    if username in database:
        print( username, "Already registered ")
        return ""
    print(username, "has been registered")
    return username



