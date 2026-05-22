
# School Management System using Inheritance

class Parent:

    def __init__(self, name, age):

        self.Name = name
        self.Age = age

    def display(self):
        print("Parent.Name = " + self.Name)
        print("Parent.Age = " + str(self.Age))

# child class Student inheriting from parent class Parent 

class Student(Parent):

    def __init__(self, name, age, marks):

        self.Marks = marks
        super().__init__(name, age)

    # method to calculate grade based on marks using if-elif-else statements

    def calculate_grade(self):

        if self.Marks >= 90:
            return "A"
        elif self.Marks >= 80:
            return "B"
        elif self.Marks >= 70:
            return "C"
        elif self.Marks >= 60:
            return "D"
        else:
            return "F"
        
    # use super() to call the parent class display method and then display marks information  
      
    def display(self):
        super().display()    
        print("Student.Marks = " + str(self.Marks))

# child class Teacher inheriting from parent class Parent

class Teacher(Parent):

        def __init__(self, name, age, subject):
            self.Subject = subject
            super().__init__(name, age)
            
        def teach(self):
            print("teacher is teaching " + self.Subject)
        
        # use super() to call the parent class display method and then display subject information
    
        def display(self):
            super().display()    
            print("Teacher.subject = " + self.Subject)  

stu1 = Student("Yashdeep", 20, 91)

stu1.display()
print("Grade =", stu1.calculate_grade())

print()

teacher1 = Teacher("Rajendra", 45, "Python")

teacher1.display()
teacher1.teach()
