class Student:
    def __init__(self, student_name, roll_number, marks):
        self.__student_name = student_name 
        self.__roll_number = roll_number
        self.__marks = 0 

     # use setter for validation

        self.set_marks(marks)    

#  Getter and Setter methods for encapsulation

    def get_student_name(self):
        return self.__student_name

    def get_roll_number(self):
        return self.__roll_number

    def get_marks(self):    
        return self.__marks 
       
# setter methods

    def set_student_name(self, new_name):
        self.__student_name = new_name

    def set_marks(self, new_marks):

        if new_marks < 0 or new_marks > 100:
            print("Invalid marks")
        else:    
            self.__marks = new_marks 

# grade method to calculate grade     

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "F"
        
# display method to show student details

    def display_student(self):
        print("student name =", self.__student_name)

        print("roll number =", self.__roll_number)

        if self.__marks < 0 or self.__marks > 100:
            print("Invalid marks")
        else:    
            print("marks =", self.__marks)    
            print("grade =",self.calculate_grade())

        
stu1 = Student("Yashdeep", 35, 91)
stu1.display_student()

print()

stu2 = Student("Rahul", 12, 50)
stu2.display_student()