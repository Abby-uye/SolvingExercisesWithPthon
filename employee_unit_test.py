import unittest
from employee import Employee


class MyTestCase(unittest.TestCase):
    def test_that_Can_set_name_and_get_name(self):
        employee = Employee(5, "john", 2000)
        self.assertEqual("john", employee.get_employee_name())

    def test_that_cannot_set_null_value_as_name(self):
        with self.assertRaises(ValueError): raise Employee()
