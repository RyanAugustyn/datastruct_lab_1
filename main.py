from implementation import *


print(months[2])

for snack in healthy_snacks:
    print(snack)

print(f"The user's name is {user_profile['First Name']} {user_profile['Last Name']}")
print(f"He can't be reached at the email {user_profile['Email Address']} nor the number {user_profile['Phone Number']}")

for relative in maybe_family:
    print(f"{relative['First name']} is my {relative['Relation']}.")