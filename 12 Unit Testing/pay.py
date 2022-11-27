class Pay:
    def __init__(self, salary):
        self._salary = salary
        self._bonus = 100

    def raise_salary(self, percentage):
        if percentage < 0 or percentage > 20:
            raise ValueError("Percentage must be between 0 and 20")
        self._salary = self._salary * (100 + percentage) / 100

    def set_bonus(self, bonus):
        if bonus < 0 or bonus > 200:
            raise ValueError("Bonus must be between 0 and 200")
        self._bonus = bonus

    def get_month_salary(self):
        return self._salary

    def get_year_salary(self):
        return self._salary * 12 + self._bonus
