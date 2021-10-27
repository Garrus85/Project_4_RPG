import random


class Hero:

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.level = 1
        self.attributes = {"HP" : 100, "Strength" : 1, "Dexterity" : 1, "Wisdom" : 1, "Luck" : 1}
        self.inventory = []


    def get_details(self):
        return f'I am {self.name} the {self.role}! I am level: {self.level}!'

    def get_attributes(self):
        attributes_string = ""
        for key in self.attributes:
            attributes_string = attributes_string + f"\n{key}: {self.attributes[key]}"
        return attributes_string

    def get_inventory(self):
        return self.inventory

    def attack_roll(self):
        pass

    def defense_roll(self):
        pass



