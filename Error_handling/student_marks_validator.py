from dataclasses import dataclass

@dataclass

class StudentMarksValidator:
    marks: int

    def check_marks(self):
        if self.marks < 0 :
            raise ValueError("negative marks are not allowed")
            
        elif self.marks > 100:
            raise ValueError("jayada shanar ban ra hai kya")
        
        else:
            return "Marks are valid"
        
student1 = StudentMarksValidator(1788)

try:
    print(student1.check_marks())

except ValueError as e:
    print(e)

finally:   
    print("validation process completed")    