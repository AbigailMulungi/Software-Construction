from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bonus(self):
        pass

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

class ReportGenerator:
    def generate_report(self, employee):
        report = f"{employee.__class__.__name__} Report: {employee.name}"
        print(report)

class BonusCalculator:
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

if __name__ == "__main__":
    manager = Manager("Alice")
    developer = Developer("Bob")

    report_generator = ReportGenerator()
    report_generator.generate_report(manager)
    report_generator.generate_report(developer)

    bonus_calculator = BonusCalculator()
    manager_bonus = bonus_calculator.calculate_bonus(manager)
    developer_bonus = bonus_calculator.calculate_bonus(developer)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
