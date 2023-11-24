from reporting import SalaryReport
from reporting import StaffingReport
from reporting import ContactReport
from contact import Contact

class Company:
    def __init__(self, name, address, phone, email, employees):
        self.name = name
        self.contact = Contact(address, phone, email)
        self.employees = employees
        self.reports = [
            SalaryReport(self.employees),
            StaffingReport(self.employees),
            ContactReport(self.employees),
        ]

    def show_company_info(self):
        print(f"Company: {self.name} ({len(self.employees)} employees)")
        print(f"Contact: {self.contact.get_contact_info()}")

        for r in self.reports:
            print()
            r.show_report()
