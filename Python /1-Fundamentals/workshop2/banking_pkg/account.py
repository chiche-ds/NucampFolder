
def show_balance(balance):
    return( float(balance))


def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    return (balance + amount)


def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))
    if balance <= 0:
        print("where are you going to get that kind of money ")
    else:
        return (balance - amount)


def logout(name):
    print("Goodbye", name)
