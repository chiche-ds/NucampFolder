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
while True:
    name = input("Enter name to register:")
    if len(name) > 10:
        print("enter name again")
        continue
    break
while True:
    pin = input("Enter PIN: ")
    try:
        pin = int(pin)
    except ValueError:
        print("Invalid You need to enter a valid number!")
        continue
    if len(str(pin)) > 4:
        print("Your PIN should not be more than 4 degits")
        continue
    break
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
        print("Current Balance: $", account.show_balance(balance))
    elif option == "2":
        print(balance)
        balance = account.deposit(balance)
        print("Current Balance : $", balance)
    elif option == "3":
        balance = account.withdraw(balance)
        print("Current Balance : $", balance )
    elif option == "4":
        account.logout(name)
    else:
        print("invalid option ")
