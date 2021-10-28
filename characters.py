import random


class Hero:

    def __init__(self, name, role):
        self.name = name
        self.inventory = []
        self.level = 1
        self.attributes = {"HP": 100, "STR": 1, "DEX": 1, "WIS": 1, "LUCK": 1}
        self.inventory = []
        if role == "S":
            self.role = "Soldier"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(20, 50)
            self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 4)
        elif role == "R":
            self.role = "Rogue"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(10, 35)
            self.attributes["DEX"] = self.attributes["DEX"] + random.randint(1, 4)
        else:
            self.role = "Adept"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(0, 20)
            self.attributes["WIS"] = self.attributes["WIS"] + random.randint(1, 4)

    def get_details(self):
        attributes_string = f'{self.name} the {self.role}: Level {self.level}.\n'
        for key in self.attributes:
            attributes_string = attributes_string + f"{key}: {self.attributes[key]}. "
        return attributes_string

    def get_inventory(self):
        return self.inventory

    def attack_roll(self):
        pass

    def defense_roll(self):
        pass
