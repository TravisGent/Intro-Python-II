# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'You currently stand in the {self.name}. {self.description}'