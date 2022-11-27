class Company:
    def __init__(self, name, address, phone, employees):
        self.name = name
        self.address = address
        self.phone = phone
        self.employees = employees

    def show_company_info(self):
        print(f"Company: {self.name}")
        print(f"Contact: {self.address}, {self.phone}")
        print()
        self.show_salaries_report()
        print()
        self.show_staffing_report()

    def show_salaries_report(self):
        print("SALARIES")
        print("========")
        for e in self.employees:
            print(f"{e.first_name} {e.last_name}, ${e.salary:.2f}")

    def show_staffing_report(self):
        print("STAFFING")
        print("========")
        for e in self.employees:
            print(f"{e.first_name} {e.last_name}, {e.get_job_title()}")
