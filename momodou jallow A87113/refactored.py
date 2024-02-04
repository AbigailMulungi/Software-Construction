from abc import ABC, abstractmethod

'''
Single Responsibility Principle (SRP): 

Employee class represents a single responsibility, 
defining basic attributes and an abstract method for role description.
'''
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role_description(self):
        pass


'''
Open/Closed Principle (OCP):

Manager and Developer classes are open for extension (can add new roles) 
but closed for modification 

NB: don't need to change existing code for new roles
'''
class Manager(Employee):
    def role_description(self):
        return "Manager"

    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def role_description(self):
        return "Developer"

    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

'''
Single Responsibility Principle (SRP) and Liskov Substitution Principle (LSP):

ReportGenerator class has a single responsibility of generating reports,
and it works with any Employee type, adhering to LSP.
'''
class ReportGenerator:
    def generate_report(self, employee):
        print(f"{employee.role_description()} Report: {employee.name}")


'''
Dependency Inversion Principle (DIP):

BonusCalculator class depends on abstractions (Employee), 
not on concrete implementations, achieving loose coupling.
'''
class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

if __name__ == "__main__":
    # Creating instances of Manager and Developer
    manager = Manager("Alice")
    developer = Developer("Bob")

    # Using ReportGenerator to generate reports for employees
    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    # Using BonusCalculator to calculate bonuses for employees
    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    # Printing bonuses for Manager and Developer
    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    # Executing role-specific methods for Manager and Developer
    manager.manage_team()
    developer.code_review()
