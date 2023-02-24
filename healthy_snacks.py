class Healthy_Snacks:
    def __init__(self) -> None:
        self.healthy_snacks = {"oranges", "radishes", "delicious beets", "kumquat", "pear"}
    
    def add_to_set(self, list: list):
        self.healthy_snacks.update(list)
    
    def print_all(self):
        for snack in self.healthy_snacks:
            print(snack)