from week2.chapter9.exercise.Admin import User


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