
def show_balance(balance):
    return (float(balance))


def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    return (float(balance) + amount)


def withdraw(balance):
    if balance <= 0:
        print("where are you going to get that kind of money ")
    else:
        amount = float(input("Enter amount to withdraw:"))
        return (float(balance) - amount)


def logout(name):
    print("Goodbye", name)
