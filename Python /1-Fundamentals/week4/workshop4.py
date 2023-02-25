
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
    def change_name(self, name ):
        self.name = name
    def change_pin(self, pin):
        self.pin = pin
        print("your pin has change to ", self.pin)
    def change_password(self, password):
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name,"has an acoount balance of: ", self.balance)
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def transfer_money(self , user , amount ):
        print("You are transfering ", amount ,"to ", user.name )
        print("authentication  is required ")
        pincode = input("Enter your PIN:")
        if pincode != self.pin:
           print("Invalid PIN. transaction canceled ")
           return False
        
        print("Transfer authorized ")
        print("Transfering ", amount, "to", user.name) 
        self.balance -= amount
        user.balance += amount


    def request_money(self, user , amount):
        print("You are requesting ",amount ,"from",user.name)
        print("Authentication is required ")
        pincode = input("Enter Your PIN: ")
        if pincode != self.pin:
            print("Pin is incorrect, authentication failed!")
            return False
        print("Authentication successful, request has been sent!")

        print(user.name, "has requested $", amount)
        print("Authentication required")
        password = (input("Please enter your password: "))
        if password != user.password:
            print("Authentication failed, transfer denied!")
        print("The transfer of $", amount, "to", user.name , "has been successful")
        self.balance += amount
        user.balance -= amount


""" Driver Code for Task 1
user1 = User("Bob", "1234", "password")

print(user1.name, user1.pin, user1.password) """

""" Driver Code for Task 2
user1 = User("Bob", "4321", "newpassword")
print(user1.name, user1.pin, user1.password) """

""" Driver Code for Task 3
user1 = BankUser("Bob", "1234", "password")
print(user1.name, user1.pin, user1.password, user1.balance)"""

""" Driver Code for Task 4
user1 = BankUser("Bob", "1234", "password")
user1.show_balance()
user1.deposit(500)
user1.show_balance()
user1.withdraw(200)
user1.show_balance()"""

""" Driver Code for Task 5"""
user1 = BankUser("Alice", "1234", "password")
user2 = BankUser("Bob", "4321","password1")

user1.deposit(10000)
user1.transfer_money(user2, -8000)
user1.show_balance()

user1.request_money(user2, 2000)
user1.show_balance()
user2.show_balance()