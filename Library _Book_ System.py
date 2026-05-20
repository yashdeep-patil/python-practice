class Book:
    def __init__(self, book_title, author_name):
        self.__book_title = book_title
        self.__author_name = author_name
        self.__availability_status = True

# getter methods

    def get__book_title(self):   
        return self.__book_title

    def get__author_name(self):
        return self.__author_name
    
    def get__availability_status(self):
        return self.__availability_status          
    
# issue book method

    def issue_book(self):
        if self.__availability_status:
            self.__availability_status = False
            print(self.__book_title + " has been issued")
        else:
            print(self.__book_title + " is already issued")    

# return book method

    def return_book(self):
        if self.__availability_status:
            print(self.__book_title + " is already available")  
        else:
             print(self.__book_title + " has been returned")
             self.__availability_status = True

# display book 

    def display_book(self):
        print("Book.title = " + self.__book_title)
        
        print("Book.author = " + self.__author_name)

        if self.__availability_status:
            print("Book.availability = Available")

        else:
            print("Book.availability = Not Available")

book1 = Book("Zero to One", "Peter Thiel")

book1.display_book()

print()

book1.issue_book()
book1.display_book()

print()

book1.issue_book()

print()

book1.return_book()
book1.display_book()

print()

book1.return_book()