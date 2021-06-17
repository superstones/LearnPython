import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """创建一个雇员对象，供使用的测试方法使用"""
        self.my_employee = Employee('shi', 'lei', 65000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 70000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 75000)
