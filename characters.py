import random


class Hero:

    def __init__(self, name, role):
        self.name = name
        self.inventory = {"Gold": 0, "Silver": 5, "Copper": 30}
        self.level = 1
        self.attributes = {"HP": 100, "AC": 10, "STR": 1, "DEX": 1, "WIS": 1, "LUCK": 1}
        self.weapon = []

        if role == "S":
            self.role = "Soldier"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(20, 50)
            self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 4)
            self.attributes["AC"] = self.attributes["AC"] + 3
            self.weapon.append(("Sword", 5))
        elif role == "R":
            self.role = "Rogue"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(10, 35)
            self.attributes["DEX"] = self.attributes["DEX"] + random.randint(1, 4)
            self.attributes["AC"] = self.attributes["AC"] + 1
            self.attributes["LUCK"] = self.attributes["LUCK"] + random.randint(1, 3)
            self.weapon.append(("Short Sword", 3))
        else:
            self.role = "Adept"
            self.attributes["HP"] = self.attributes["HP"] + random.randint(0, 20)
            self.attributes["WIS"] = self.attributes["WIS"] + random.randint(1, 6)
            self.attributes["LUCK"] = self.attributes["LUCK"] + random.randint(1, 2)
            self.weapon.append(("Staff", 3))

    def get_details(self):
        attributes_string = f'{self.name} the {self.role}: Level {self.level}.\n'
        for key in self.attributes:
            attributes_string = attributes_string + f"{key}: {self.attributes[key]}. "
        return attributes_string


    def return_hp(self):
        return self.attributes["HP"]

    @property
    def get_inventory(self):
        return "".join(f'{key}: {self.inventory[key]}.' for key in self.inventory)


    def collect_loot(self, loot):
        """TODO: update inventory with new loot if key not already in dictionary"""
        for key in loot:
            if key in self.inventory:
                self.inventory[key] = self.inventory[key] + loot[key]


    def equipped_weapon(self):
        return self.weapon[0][0]


    def attack_roll(self):
        #TODO: edit rolls for STR, DEX, WIS, LUCK
        return self.attributes.get("STR") + random.randint(1,20)


    def defense_roll(self):
        luck_roll = random.randint(self.attributes.get("LUCK"), 20)
        if luck_roll != 20:
            return self.attributes.get("AC")
        print("You dodged the attack!")
        return self.attributes.get("AC") + 20


    def damage_roll(self, roll=0):
        dmg = self.weapon[0][1] + self.attributes.get("STR") + random.randint(1, 6)
        if roll - self.attributes.get("STR") != 20:
            return dmg
        print("CRITICAL HIT!")
        return dmg * 2


    def damage_taken(self, dmg):
        self.attributes["HP"] = self.attributes["HP"] - dmg
        return f'Your HP is now {self.attributes["HP"]}'




class NPC:
    def __init__(self, type):
        self.name = type
        self.attributes = {"HP": 75, "AC": 10, "STR": 1, "DEX": 1, "WIS": 1, "LUCK": 1}
        self.inventory = {"Gold": 0, "Silver": 0, "Copper": 0}
        self.weapon = []

    @property
    def get_inventory(self):
        return " ".join(f'{key}: {self.inventory[key]} ' for key in self.inventory if self.inventory[key] > 0)

    def return_hp(self):
        return self.attributes["HP"]

    def attack_roll(self):
        return self.attributes.get("STR") + random.randint(1, 20)

    def defense_roll(self):
        return self.attributes.get("AC")

    def damage_roll(self, roll):
        dmg = self.weapon[0][1] + self.attributes.get("STR") + random.randint(1, 6)
        if roll - self.attributes.get("STR") == 20:
            return dmg * 2
        else:
            return dmg

    def damage_taken(self, dmg):
        self.attributes["HP"] = self.attributes["HP"] - dmg
        return f'The {self.type}s HP is {self.attributes["HP"]}'



class Daamon(NPC):
    def __init__(self, type):
        self.type = type
        super().__init__(self)
        self.attributes["HP"] = self.attributes["HP"] + random.randint(15, 25)
        self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 2)
        self.inventory["Copper"] = self.inventory["Copper"] + random.randint(1, 20)
        self.weapon.append(["Barbed Club", 4])