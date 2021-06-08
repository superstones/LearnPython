from User import User
from privileges import Admin
from privileges import Privileges

my_admi = User('shi', 'lei', '23', ' male')

my_admi.describe_user()
my_admi = Privileges()
my_admi.show_privileges()
