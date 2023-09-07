# A Simple Banking system using python oops 

import time

#parent class
class User:
    def __init__(self, name, age, gender):
        self.name=name
        self.gender=gender
        self.age=age

    def info(self):
        print("--Account holder Details--")
        print("")
        print("Name   :",self.name)
        print("Age    :",self.age)
        print("Gender :",self.gender)

#child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    # Deposit Method
    def deposit(self,amount):
        self.balance= self.balance + amount
        print("----------------------->Account balance has been updated<-----------------------")
        print(f"\n-----------> {amount} is been added to the account of {self.name}")
        print(f"-----------> Total balance : {self.balance} \n")

    # Withdraw Method
    def withdraw(self,amount):
        if(self.balance < amount):
            print("Insufficient balance")
        else:
            self.balance= self.balance - amount
            print("withdraw is under proces. Please wait!")
            time.sleep(2)
            print("----------------------->Account balance has been updated<-----------------------")
            print(f"\n-----------> {amount} has been withdrawn ")
            print(f"-----------> Total balance : {self.balance} \n")

        return amount

    # View balance method
    def view_balance(self):
        self.info()
        print(f"\nTotal balance : {self.balance} \n")
        

# Drive Code

ac1= Bank("Yaswanth",19,"Male")
ac1.deposit(9000)

ac2= Bank("Ana",20,"Female")
ac2.deposit(7000)

ac2.deposit(ac1.withdraw(1000))

ac1.view_balance()
ac2.view_balance()

