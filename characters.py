import random


class Hero:

    def __init__(self, name, role):
        self.name = name
        self.inventory = {}
        self.level = 1
        self.attributes = {"HP": 100, "AC": 10, "STR": 1, "DEX": 1, "WIS": 1, "LUCK": 1}

        if role == "S":
            self.role = "Soldier"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(20, 50)
            self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 4)
            self.attributes["AC"] = self.attributes["AC"] + 3
            self.weapon = {"Sword", 5}
        elif role == "R":
            self.role = "Rogue"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(10, 35)
            self.attributes["DEX"] = self.attributes["DEX"] + random.randint(1, 4)
            self.attributes["AC"] = self.attributes["AC"] + 1
            self.attributes["LUCK"] = self.attributes["LUCK"] + random.randint(1, 3)
            self.weapon = {"Short Sword", 3}
        else:
            self.role = "Adept"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(0, 20)
            self.attributes["WIS"] = self.attributes["WIS"] + random.randint(1, 4)
            self.attributes["LUCK"] = self.attributes["LUCK"] + random.randint(1, 3)
            self.weapon = {"Staff", 3}

    def get_details(self):
        attributes_string = f'{self.name} the {self.role}: Level {self.level}.\n'
        for key in self.attributes:
            attributes_string = attributes_string + f"{key}: {self.attributes[key]}. "
        return attributes_string

    def get_inventory(self):
        return self.inventory

    def attack_roll(self):
        """NEED TO EDIT ROLLS FOR LUCK"""
        return self.attributes.get("STR") + random.randint(1,20)

    def defense_roll(self):
        return self.attributes.get("AC")

    def damage_roll(self):
        return self.weapon.get("Sword") + self.attributes.get("STR") + random.randint(1, 6)

    def damage_taken(self, dmg):
        self.attributes["HP"] = self.attributes["HP"] - dmg
        return f'Your HP is {self.attributes["HP"]}'



class NPC:
    def __init__(self, type):
        self.name = type
        self.attributes = {"HP": 75, "AC": 10, "STR": 1, "DEX": 1, "WIS": 1, "LUCK": 1}
        self.inventory = {"Gold": 0, "Silver": 0, "Copper": 0}



    def see_inventory(self):
        return "".join(f'{key}: {self.inventory[key]}.' for key in self.inventory)

    def attack_roll(self):
        return self.attributes.get("STR") + random.randint(1,20)

    def defense_roll(self):
        return self.attributes.get("AC")

    def damage_roll(self):
        return self.weapon.get("Barbed Club") + self.attributes.get("STR")


    def damage_taken(self, dmg):
        self.attributes["HP"] = self.attributes["HP"] - dmg
        return f'The {self.type}s HP is {self.attributes["HP"]}'


class Daamon(NPC):
    def __init__(self):
        super().__init__(self)
        self.attributes["HP"] = self.attributes["HP"] + random.randint(15, 25)
        self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 2)
        self.inventory["Copper"] = self.inventory["Copper"] + random.randint(1, 20)
        self.weapon = {"Barbed Club", 4}