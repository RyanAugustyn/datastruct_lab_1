class Maybe_Family():
    def __init__(self) -> None:
        self.maybe_family_list = [
    {"First name" : "Jack", 
     "Last name" : "Sparrow", 
     "Relation" : "mother's brother's third cousin"
     },
    {"First name" : "Dwane", 
     "Last name" : "Johnson", 
     "Relation" : "great great granduncle's third cousin"
     },
    {"First name" : "Flannery", 
     "Last name" : "O'Connor", 
     "Relation" : "great great aunt's...third cousin"
     }
    ]

    def print_relations(self):
        for relative in self.maybe_family_list:
            print(f"{relative['First name']} is my {relative['Relation']}.")