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




