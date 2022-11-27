from employee import Manager
from employee import Cook
from employee import Mechanic
from employee import TowTruckDriver
from company import Company

employees = [
    Manager("Vera", "Schmidt", "Main Street 3, Deer Creek", "044-4203", 2000),
    Cook("Roberto", "Castillo", "Market Road 40, Dalby Springs", "038-2201", 2100),
    Mechanic("Dave", "Dreissig", "Blue Square 21, Hope Village", "037-9820", 2200),
    Mechanic("Tina", "River", "Oak Boulevard 67, Hope Village", "037-1245", 2300),
    Mechanic("Ken", "Parker", "First Street 2, Hope Village", "037-2355", 1900),
    Mechanic("Chuck", "Rainey", "Rose Street 26, Deer Creek", "044-7345", 1800),
    TowTruckDriver("Rufus", "Roscoe", "Chester Road 12, Dalby Springs", "038-2355", 1850),
]

company = Company("Star Station", "Rocky Road 1, Deer Creek", "044-2354", employees)

company.show_company_info()
