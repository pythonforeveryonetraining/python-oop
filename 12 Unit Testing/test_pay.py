import unittest
from pay import Pay


class TestPay(unittest.TestCase):
    def test_monthly_salary(self):
        p = Pay(2000)
        self.assertEqual(p.get_month_salary(), 2000)

    def test_yearly_salary(self):
        p = Pay(2000)
        self.assertEqual(p.get_year_salary(), 24100)

    def test_raise_salary(self):
        p = Pay(2000)
        p.raise_salary(10)
        self.assertEqual(p.get_month_salary(), 2200)

    def test_add_bonus(self):
        p = Pay(2000)
        p.set_bonus(200)
        self.assertEqual(p.get_year_salary(), 24200)
