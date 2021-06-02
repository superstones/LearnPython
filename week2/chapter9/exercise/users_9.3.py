class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print("\nfirst_name:" + self.first_name.title())
        print("last_name:" + self.last_name.title())
        print("age:" + self.age.title())
        print("sex:" + self.sex.title())

    def greet_user(self):
        full_name = self.first_name + '' + self.last_name
        print("Hello, " + full_name.title())


my_user = User('shi', 'lei', '25', 'male')
my_user.describe_user()
my_user.greet_user()
her_user = User('c', 'hr', '24', 'fmale')
her_user.describe_user()
her_user.greet_user()