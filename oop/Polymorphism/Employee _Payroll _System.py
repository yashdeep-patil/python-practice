
from dataclasses import dataclass

@dataclass
class Employee:
  
  name:str
  employee_id:int
  salary:float

  def calculate_salary(self):
    return self.salary

@dataclass

class FullTimeEmployee(Employee):
  bonus:float

  def calculate_salary(self):
   final_salary = self.salary + self.bonus
   return final_salary

@dataclass

class PartTimeEmployee(Employee):
   hours_worked:float
   hourly_rate:float

   def calculate_salary(self):
    final_salary = self.hours_worked * self.hourly_rate
    return final_salary
    

emp1 = FullTimeEmployee("Yashdeep", 101, 50000, 10000)

print("Employee Name =", emp1.name)
print("Final Salary =", emp1.calculate_salary())

print()


emp2 = PartTimeEmployee("Rahul", 102, 0, 40, 500)

print("Employee Name =", emp2.name)
print("Final Salary =", emp2.calculate_salary())    