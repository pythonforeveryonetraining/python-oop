from reporting import SalaryReport
from reporting import StaffingReport
from reporting import ContactReport
from contact import Contact

class Company:
    def __init__(self, name, address, phone, email, employees):
        self.name = name
        self.contact = Contact(address, phone, email)
        self._employees = employees
        self._reports = [
            SalaryReport(self._employees),
            StaffingReport(self._employees),
            ContactReport(self._employees),
        ]

    def show_company_info(self):
        print(f"Company: {self.name} ({len(self._employees)} employees)")
        print(f"Contact: {self.contact.get_contact_info()}")

        for r in self._reports:
            print()
            r.show_report()

    def raise_all_salaries(self, percentage):
            for e in self._employees:
                e.pay.raise_salary(percentage)

    def set_all_bonuses(self, bonus):
        for e in self._employees:
            e.pay.set_bonus(bonus)                
