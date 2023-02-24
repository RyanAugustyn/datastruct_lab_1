class User_Profile():
    def __init__(self) -> None:
        self.user_profile =  {
    "First Name" : "John",
    "Last Name" : "Cleese",
    "Email Address" : "deadparrot@wandafish.com",
    "Phone Number" : "mindyourbusiness"
}

    def print_info(self):
        print(f"The user's name is {self.user_profile['First Name']} {self.user_profile['Last Name']}")
        print(f"He can't be reached at the email {self.user_profile['Email Address']} nor the number {self.user_profile['Phone Number']}")
