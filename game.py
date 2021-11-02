import time


def intro():

    print(" ---------------------------- ")
    print(" -------------THE------------ ")
    print(" --- COMPENDIUM OF POWER ---- ")
    print(" ---------------------------- ")
    time.sleep(1)
    while True:
        name = input("Character Name: ").capitalize()
        confirm_name = input(f"Confirm your name is {name}? Y/N ").upper()
        if confirm_name == "Y":
            break
        else:
            continue

    while True:
        print("""Choose your class?
            [S] SOLDIER
            [R] ROGUE
            [A] ADEPT""")
        role = input().upper()
        if role == "S":
            print("SOLDIER: Specializes in melee weapons, shields and armour. ")
            time.sleep(1)
            print("Confirm choice: SOLDIER? Y/N")
            confirm = input("").upper()
            if confirm == "Y":
                return name, role
            else:
                continue
        elif role == "R":
            print("ROGUE: Specializes in ranged combat, stealth, traps and poisons. ")
            time.sleep(1)
            print("Confirm choice: ROGUE? Y/N")
            confirm = input("").upper()
            if confirm == "Y":
                return name, role
            else:
                continue
        elif role == "A":
            print("ADEPT: Specializes in manipulating the Fringes of Power. ")
            time.sleep(1)
            print("Confirm choice: ADEPT? Y/N")
            confirm = input("").upper()
            if confirm == "Y":
                return name, role
            else:
                continue
        else:
            print("Invalid input. Choice is either [S], [R] or [A]")
            continue



def combat(hero, enemy):
    """NEED TO GET HERO AND ENEMY HP AND MAKE WHILE STATEMENT"""
    hero_hp = hero.
    print("You attack the daamon!")
    attack_roll = hero.attack_roll()
    print(f'You rolled {attack_roll}')
    defense_roll = enemy.defense_roll()
    if attack_roll > defense_roll:
        print("Your attack slices into the daamon's left arm")
    else:
        print("Your attack narrowly misses the daamon's throat")
