class Employee():
    """一个表示雇员的类"""

    def __init__(self, first_name, last_name, salary):
        """初始化雇员"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
