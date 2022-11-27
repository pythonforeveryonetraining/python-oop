from employee import Employee
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from employee import TowTruckDriver
from company import Company

employees = [
    Manager("Vera", "Schmidt", 2000),
    Attendant("Chuck", "Murphy", 1800),
    Attendant("Samantha", "Carrington", 1800),
    Cook("Roberto", "Castillo", 2100),
    Mechanic("Dave", "Dreissig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic("Ken", "Parker", 1900),
    Mechanic("Chuck", "Rainey", 1800),
    TowTruckDriver("Rufus", "Roscoe", 1850),
]

company = Company("Star Station", "Rocky Road 1, Deer Creek", "044-2354", employees)

print(f"Company: {company.name}")
print(f"Contact: {company.address}, {company.phone}")
print()
for e in company.employees:
    print(f"{e.first_name} {e.last_name}, ${e.salary:.2f}, {e.get_job_title()}")

