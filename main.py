from months import Months
from healthy_snacks import Healthy_Snacks
from user_profile import User_Profile
from maybe_family import Maybe_Family

month1 = Months()
month1.print_pi_month()

hsnacks = Healthy_Snacks()
hsnacks.add_to_set(["mango", "bannana", "broccoli", "peas"])
hsnacks.print_all()

user = User_Profile()
user.print_info()

family = Maybe_Family()
family.print_relations()
