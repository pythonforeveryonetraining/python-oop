class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

employees = [
    Employee("Vera", "Schmidt", 2000),
    Employee("Chuck", "Murphy", 1800),
    Employee("Samantha", "Carrington", 1800),
    Employee("Roberto", "Castillo", 2100),
    Employee("Dave", "Dreissig", 2200),
    Employee("Tina", "River", 2300),
    Employee("Ken", "Parker", 1900),
    Employee("Chuck", "Rainey", 1800),
]

for e in employees:
    print(f"{e.first_name} {e.last_name}, ${e.salary:.2f}")
