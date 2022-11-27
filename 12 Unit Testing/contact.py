class Contact:
    def __init__(self, address, phone, email):
        self._address = address
        self._phone = phone
        self._email = email

    def get_contact_info(self):
        return f"{self._address}, {self._phone}, {self._email}"
