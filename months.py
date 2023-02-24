class Months:
    def __init__(self) -> None:
        self.months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

    def print_pi_month(self):
        index = int(3.14) - 1
        temp = self.months[index]
        print(temp)