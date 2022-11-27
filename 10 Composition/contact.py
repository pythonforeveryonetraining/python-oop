class Contact:
    def __init__(self, address, phone, email):
        self.address = address
        self.phone = phone
        self.email = email

    def get_contact_info(self):
        return f"{self.address}, {self.phone}, {self.email}"
