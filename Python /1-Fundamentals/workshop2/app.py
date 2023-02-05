from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:")
pin = int(input("Enter PIN: "))
balance = 0

print(name, "has been registered with a string balance of $", balance)

while True:
    print("LOGIN")
    name_to_validate = input("Enter name:")
    pin_to_validate = int(input("Enter PIN: "))
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid Credentials")

while True:
    atm_menu(name)
    option = input("Choose an option:")
    if option == "1":
        print("Current Balance: $",account.show_balance(balance))
    elif option == "2":
        print("Current Balance : $", account.deposit(balance))
    elif option == "3":
        print("Current Balance : $", account.withdraw(balance))
    elif option == "4":
        account.logout(name)
    else:
        print("invalid option ")
