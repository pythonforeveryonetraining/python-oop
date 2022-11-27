class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

class Manager(Employee):
    def get_job_title(self):
        return "Manager"

class Attendant(Employee):
    def get_job_title(self):
        return "Station Attendant"

class Cook(Employee):
    def get_job_title(self):
        return "Cook"

class Mechanic(Employee):
    def get_job_title(self):
        return "Mechanic"

class TowTruckDriver(Employee):
    def get_job_title(self):
        return "Tow Truck Driver"
