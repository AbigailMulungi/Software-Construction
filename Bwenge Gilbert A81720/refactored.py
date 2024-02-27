from abc import ABC, abstractmethod

# Define base class for all employees
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bonus(self):
        pass

# Define separate classes for Manager and Developer
class Manager(Employee):
    def calculate_bonus(self):
        return 1000

    def manage_team(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    def calculate_bonus(self):
        return 500

    def code_review(self):
        print(f"{self.name} is conducting a code review.")

# Define separate classes for report generation
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, employee):
        pass

class ManagerReportGenerator(ReportGenerator):
    def generate_report(self, manager):
        print(f"Manager Report: {manager.name}")

class DeveloperReportGenerator(ReportGenerator):
    def generate_report(self, developer):
        print(f"Developer Report: {developer.name}")

# Define separate class for bonus calculation
class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    report_generator_manager = ManagerReportGenerator()
    report_generator_developer = DeveloperReportGenerator()

    report_generator_manager.generate_report(manager)
    report_generator_developer.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
