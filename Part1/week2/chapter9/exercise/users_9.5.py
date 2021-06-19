class User():
    def __init__(self, first_name, last_name, age, sex, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\nfirst_name:" + self.first_name.title())
        print("last_name:" + self.last_name.title())
        print("age:" + self.age.title())
        print("sex:" + self.sex.title())
        print("login_attempts:" + str(self.login_attempts))

    def greet_user(self):
        full_name = self.first_name + '' + self.last_name
        print("Hello, " + full_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


my_user = User('shi', 'lei', '25', 'male', 0)
my_user.increment_login_attempts()
my_user.describe_user()
my_user.reset_login_attempts()
my_user.describe_user()
