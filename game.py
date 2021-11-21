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


def game_over():
    print("You have died")
    time.sleep(2)
    print(" ---------------------------- ")
    print(" -------- GAME OVER --------- ")
    print(" ---------------------------- ")


def combat(hero, enemy):
    #TODO: Offer options after round of combat: attack, run, use item etc
    hero_hp = hero.return_hp()
    enemy_hp = enemy.return_hp()

    while hero_hp > 0 or enemy_hp > 0:

        print(f'\nYou attack the {enemy.type}!')
        hero_attack_roll = hero.attack_roll()
        time.sleep(1)
        print(f'You rolled {hero_attack_roll}')
        enemy_defense_roll = enemy.defense_roll()
        time.sleep(1)
        if hero_attack_roll > enemy_defense_roll:
            print("Your attack hits!")
            enemy.speech_on_dmg()
            time.sleep(1)
            dmg = hero.damage_roll(hero_attack_roll)
            print(f'You deal {dmg} points of damage.')
            print(enemy.damage_taken(dmg))
            enemy_hp -= dmg
        else:
            print("Your attack missed.")
        time.sleep(2)

        if enemy_hp <= 0:
            break

        print("\nThe enemy attacks!")
        time.sleep(1)
        enemy_attack_roll = enemy.attack_roll()
        print(f'The enemy rolled {enemy_attack_roll}')
        time.sleep(1)
        hero_defense_roll = hero.defense_roll()
        if enemy_attack_roll > hero_defense_roll:
            print("You have been hit!")
            enemy_dmg = enemy.damage_roll(enemy_attack_roll)
            hero.damage_taken(enemy_dmg)
            print(f'You take {enemy_dmg} points of damage.')
        else:
            print("The attack missed")
        time.sleep(1)

    if hero_hp == 0:
        game_over()
    else:
        print(f'Your HP is {hero_hp}')
        hero.update_hp(hero_hp)
        loot = enemy.get_inventory
        print(f'The enemy dropped {loot}')
        return hero


def menu(hero):
    print("""
    [C] CONTINUE
    [I] INVENTORY
    [S] SAVE GAME
    """)
    time.sleep(1)
    choice = input().upper()
    if choice == "C":
        return
    elif choice == "I":
        print(hero.get_details())
        time.sleep(1)
       #print(f'Your HP is: {hero.return_hp()}')
        print(hero.get_inventory())
        time.sleep(1)
        return
    elif choice == "S":
        #TODO: IMPLEMENT SAVE FUNCTION
        menu(hero)
    else:
        print("Invalid choice")


def combat_choice(hero):
    # TODO: TO BE ADDED TO BEGINNING OF COMBAT
    print("""Action required! \n
    [A] ATTACK
    [T] TALK
    [I] USE ITEM
    [F] FLEE
    """)
    choice = input().upper()

    if choice == "F":
        pass
    elif choice == "T":
        pass
    elif choice == "I":
        pass
    elif choice == "I":
        pass
    else:
        print("Invalid choice")

