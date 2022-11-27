class Report:
    def __init__(self, employees):
        self.employees = employees

class SalaryReport(Report):
    def show_report(self):
        print("SALARIES")
        print("========")
        for e in self.employees:
            print(f"{e.get_full_name()}, ${e.salary:.2f}")

class StaffingReport(Report):
    def show_report(self):
        print("STAFFING")
        print("========")
        for e in self.employees:
            print(f"{e.get_full_name()}, {e.get_job_title()}")

class ContactReport(Report):
    def show_report(self):
        print("CONTACT")
        print("=======")
        for e in self.employees:
            print(f"{e.get_full_name()}, {e.address}, {e.phone}")
