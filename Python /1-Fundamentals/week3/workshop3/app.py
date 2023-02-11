from donations_pkg import homepage, user
#variables 
database = {
    "admin":"password123",
}
donations = [ ]
authorized_user = ""



#handle user input 
while True:
    homepage.show_homepage()
    if authorized_user == "":
        print("You most be logged in to donate.")
    else:
        print("Login in as:",authorized_user)
    choice = int(input("Choose an option "))
    #handle user input 
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password ")
        authorized_user = user.login(database,username,password)
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password ")
        authorized_user = user.register(database,username)
        if authorized_user != "":
            database[username] = password
    elif choice == 3:
        if authorized_user is "":
            print("You are not logged in.")
        else:
            donation_string = user.donate(authorized_user)
            donations.append(donation_string)
    elif choice == 4:
        homepage.show_donations(donations)
    elif choice == 5:
        print("a goodbye message and end the program.")
        break
    else:
        print("invalide option")
