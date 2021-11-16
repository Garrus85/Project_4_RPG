import random


class Hero:

    """Class which contains all the mechanics for the hero"""

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
        hero_attributes = f'{self.name} the {self.role}: Level {self.level}.\n'
        for key in self.attributes:
            hero_attributes = hero_attributes + f'{key}: {self.attributes[key]}. '
        return hero_attributes


    def return_hp(self):
        return self.attributes["HP"]

    def update_hp(self, health):
        #TODO: update HP not working
        self.attributes["HP"] = health


    #@property  - CAUSES STR NOT CALLABLE ERROR
    def get_inventory(self):
        return "".join(f'{key}: {self.inventory[key]}. ' for key in self.inventory)


    def collect_loot(self, loot):
        """TODO: update inventory with new loot if key not already in dictionary"""
        for key in loot:
            if key in self.inventory:
                self.inventory[key] = self.inventory[key] + loot[key]


    def equipped_weapon(self):
        return self.weapon[0][0]


    def attack_roll(self):
        #TODO: edit rolls for STR, DEX, WIS, LUCK
        return self.attributes.get("STR") + random.randint(1, 20)


    def defense_roll(self):
        luck_roll = random.randint(self.attributes.get("LUCK"), 20)
        if luck_roll != 20:
            return self.attributes.get("AC")
        print("------ DODGE ------")
        return self.attributes.get("AC") + 20


    def damage_roll(self, roll=0):
        dmg = self.weapon[0][1] + self.attributes.get("STR") + random.randint(1, 6)
        if roll - self.attributes.get("STR") != 20:
            return dmg
        print("------ CRITICAL HIT! ------")
        return dmg * 2


    def damage_taken(self, dmg):
        self.attributes["HP"] = self.attributes["HP"] - dmg
        return f'Your HP is now {self.attributes["HP"]}'




class NPC:

    """
    This is the generic NPC starting parent class. Will be used to define enemy NPCs
    Contains mechanics for enemy encounters
                                                                                """

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

    """The first enemy class - uses NPC class as its parent"""

    def __init__(self, type):
        self.type = type
        super().__init__(self)
        self.attributes["HP"] = self.attributes["HP"] + random.randint(15, 25)
        self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 2)
        self.inventory["Copper"] = self.inventory["Copper"] + random.randint(1, 20)
        self.weapon.append(["Barbed Club", 4])


class Military_Human(NPC):

    """The basis for human Military NPCs - uses NPC class as its parent"""

    def __init__(self, type):
        self.type = type
        super().__init__(self)
        self.attributes["STR"] = self.attributes["STR"] + random.randint(1, 2)
        self.attributes["WIS"] = self.attributes["WIS"] + random.randint(1, 2)
        self.inventory["Copper"] = self.inventory["Copper"] + random.randint(7, 28)
        self.weapon.append(["Fists", 1])

    def speech_on_dmg(self):
        x = random.randint(1, 3)
        if x == 1:
            print("Aaargh, I think you broke my nose!")
        elif x == 2:
            print("Ugh! That was a lucky shot")
        else:
            print("I won't let you beat me")

    def speech_on_attack(self):
        y = random.randint(1, 3)
        if y == 1:
            print("Ha! Get up from that one")
        elif y == 2:
            print("I think I just rearranged your face")
        else:
            print("If you don't back down now, you'll loose even more teeth!")