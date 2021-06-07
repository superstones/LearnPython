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


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = []

    def show_privileges(self):
        print("\nThe following user`s privileges:")
        for privilege in self.privileges:
            print("- " + privilege.title())


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege.title())
        else:
            print("- This user has no privileges.")


my_admin = Admin('shi', 'lei', '24', 'male')
my_admin.describe_user()
admin_privileges = Privileges()
admin_privileges.show_privileges()
print("\nAdding privileges...")
my_admin.privileges = ['can add post', 'can delete post', 'can ban user']
admin_privileges.show_privileges()
