from reporting import SalaryReport
from reporting import StaffingReport
from reporting import ContactReport

class Company:
    def __init__(self, name, address, phone, employees):
        self.name = name
        self.address = address
        self.phone = phone
        self.employees = employees
        self.reports = [
            SalaryReport(self.employees),
            StaffingReport(self.employees),
            ContactReport(self.employees),
        ]

    def show_company_info(self):
        print(f"Company: {self.name} ({len(self.employees)} employees)")
        print(f"Contact: {self.address}, {self.phone}")

        for r in self.reports:
            print()
            r.show_report()
