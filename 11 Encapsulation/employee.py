from contact import Contact
from pay import Pay

class Employee:
    def __init__(self, first_name, last_name, address, phone, email, salary):
        self._first_name = first_name
        self._last_name = last_name
        self.contact = Contact(address, phone, email)
        self.pay = Pay(salary)

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

class Manager(Employee):
    def get_job_title(self):
        return "Manager"

class Cook(Employee):
    def get_job_title(self):
        return "Cook"

class Mechanic(Employee):
    def get_job_title(self):
        return "Mechanic"

class TowTruckDriver(Employee):
    def get_job_title(self):
        return "Tow Truck Driver"
