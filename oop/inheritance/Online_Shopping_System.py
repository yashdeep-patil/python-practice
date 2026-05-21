class Product:

    def __init__(self, name , price):

        self.Name = name
        self.Price = price 

    def display(self):
        print("Product.Name = " + self.Name)
        print("Product.Price = " + str(self.Price))


class Electronics(Product):

    def __init__(self, name, price, warranty):
        
        super().__init__(name, price)
        self.Warranty = warranty

    def final_price(self):

        final_price = self.Price + (self.Price * 0.18) 
        return final_price

    def display(self):
        super().display()
        print("Electronics.Warranty = " + str(self.Warranty))    

class Clothing(Product):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.Size = size

    def final_price(self):

        final_price = self.Price - (self.Price * 0.10) 
        return final_price


    def display(self):
        super().display()
        print("Clothing.Size = " + self.Size)



laptop = Electronics("Laptop", 50000, "2")

laptop.display()
print("Final Price =", laptop.final_price())

print()

shirt = Clothing("T-Shirt", 2000, "XL")

shirt.display()
print("Final Price =", shirt.final_price())        