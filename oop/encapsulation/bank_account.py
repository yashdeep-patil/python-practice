class bank():
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance   

    def deposit(self, amount):
        if amount <= 0:
            print("invalid amount")
        else:
          self.__balance += amount

    def withdraw(self, amount):  

        if amount <= 0:
            print("invalid amount")
        elif amount > self.__balance:
            print("insufficient balance")
        else:
            self.__balance -= amount
            print("withdraw successful")

    def set_name(self, new_name):
           self.__name = new_name

    def display(self):      
        print("name", self.__name)  
        print("balance", self.__balance)    

acc1 = bank("yashdeep", 2000)
acc1.deposit(1000)
acc1.withdraw(500)
acc1.display()