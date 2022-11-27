class Report:
    def __init__(self, employees):
        self._employees = employees

class SalaryReport(Report):
    def show_report(self):
        print("SALARIES")
        print("========")
        for e in self._employees:
            print(f"{e.get_full_name()}, Month: ${e.pay.get_month_salary():.2f}, Year: ${e.pay.get_year_salary():.2f}")
            
class StaffingReport(Report):
    def show_report(self):
        print("STAFFING")
        print("========")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.get_job_title()}")

class ContactReport(Report):
    def show_report(self):
        print("CONTACT")
        print("=======")
        for e in self._employees:
            print(f"{e.get_full_name()}, {e.contact.get_contact_info()}")
