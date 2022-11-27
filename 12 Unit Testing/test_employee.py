import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("Albert", "Einstein", None, None, None, None)
        self.assertEqual(e.get_full_name(), "Albert Einstein")
