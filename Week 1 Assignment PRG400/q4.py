class Employee:
    def __init__(self, salary):
        self.__salary = salary  

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

emp = Employee(25000)

try:
    print(emp.__salary)  
except AttributeError:
    print("Cannot access __salary directly due to encapsulation!")

print("Current Salary:", emp.get_salary())
emp.set_salary(30000)
print("Updated Salary:", emp.get_salary())
