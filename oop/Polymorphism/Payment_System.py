class Payment:

    def __init__(self, payment_id, amount):
        self.__payment_id = payment_id
        self.__amount = amount

    def get_Payment_id(self):
        return self.__payment_id

    def get_Amount(self):
        return self.__amount
    
    def pay(self):
        print("Processing payment...")

    def display(self):
        print("Payment.Payment_id = " + self.__payment_id)
        print("Payment.Amount = " + str(self.__amount))


class UPI(Payment):

    def __init__(self, payment_id, amount, upi_id):
        super().__init__(payment_id, amount)
        self.__UPI_id = upi_id

    def get_UPI_id(self):
        return self.__UPI_id    
    
    def pay(self):
        print("Payment done using UPI")

    def transaction_fee(self):
        fee = self.get_Amount() * 0
        return fee    
    
    def display(self):
        super().display()  
        print("UPI.UPI_id = " + self.__UPI_id)


class CreditCard(Payment):
     
    def __init__(self, payment_id, amount, card_number):
         super().__init__(payment_id, amount)
         self.__card_number =  card_number

    def get_card_number(self):
        return self.__card_number
    
    def pay(self):
        print("Payment done using Credit Card")

    def transaction_fee(self):
        fee = self.get_Amount() * 0.02
        return fee 
      
    def display(self):
        super().display()
        print("CreditCard.card_number = " + self.__card_number)
        

class Wallet(Payment):

    def __init__(self, payment_id, amount, wallet_name):
        super().__init__(payment_id, amount)
        self.__wallet_name = wallet_name

    def get_Wallet_name(self):
        return self.__wallet_name
          
    def pay(self):
        print("Payment done using Wallet")

    def transaction_fee(self):
        fee = self.get_Amount() * 0.01
        return fee     

    def display(self):
        super().display()
        print("Wallet.Wallet_name = " + self.__wallet_name)



upi1 = UPI("P101", 5000, "yashdeep@upi")

upi1.display()
upi1.pay()
print("Transaction Fee =", upi1.transaction_fee())

print()


card1 = CreditCard("P102", 10000, "987654321234")

card1.display()
card1.pay()
print("Transaction Fee =", card1.transaction_fee())

print()


wallet1 = Wallet("P103", 3000, "Paytm")

wallet1.display()
wallet1.pay()
print("Transaction Fee =", wallet1.transaction_fee())        