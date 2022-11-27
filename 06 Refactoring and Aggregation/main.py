from employee import Employee
from company import Company

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

company = Company("Star Station", "Rocky Road 1, Deer Creek", "044-2354", employees)

print(f"Company: {company.name}")
print(f"Contact: {company.address}, {company.phone}")
print()
for e in company.employees:
    print(f"{e.first_name} {e.last_name}, ${e.salary:.2f}")
