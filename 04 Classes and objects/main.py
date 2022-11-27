class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [
    Employee("Vera", 2000),
    Employee("Chuck", 1800),
    Employee("Samantha", 1800),
    Employee("Roberto", 2100),
    Employee("Dave", 2200),
    Employee("Tina", 2300),
    Employee("Ken", 1900),
]

for e in employees:
    print(f"{e.name}, ${e.salary:.2f}")
