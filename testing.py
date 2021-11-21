import random
import characters
import game
import soldier


# --------TESTS-------
hero = characters.Hero("Bjorn", "S")
#soldier.soldierB2(hero)


sergeant = characters.Military_Human("Sergeant")
#sergeant.speech_on_dmg()
#print(sergeant.type)

#soldier.soldierB1(hero, "a3"      # TEST PASS
#print(hero.return_hp())
#hero.update_hp(300)               # TEST PASS
#print(hero.return_hp())
#game.menu(hero)                   # TEST PASS
# print(hero.get_details())        # TEST PASS
# print(hero.attributes            # TEST PASS
# print(hero.attack_roll())        # TEST PASS
# print(hero.damage_taken(22))     # TEST PASS
# print(hero.damage_roll())        # TEST PASS
#print(hero.get_inventory())      # TEST PASS
# print(hero.equipped_weapon())    # TEST PASS
#

daamon = Daamon("Daamon")
#print(daamon.get_inventory)  # TEST PASS
# print(daamon.attack_roll())        #TEST PASS
# print(daamon.defense_roll())       #TEST PASS
# print(daamon.damage_roll())        #TEST PASS
# print(daamon.damage_taken(20))     #TEST PASS

#   LOOT MECHANICS
#loot = daamon.get_inventory
#print(loot)                         #TEST PASS
#inv = hero.get_inventory()
#print(inv)                          #TEST PASS
#hero.collect_loot(loot)
#inv2 = hero.get_inventory()
#print(inv2)                         #TEST PASS



import characters
import time
import game


def story(hero):
    print(hero.get_details())
    time.sleep(1)

    print("""
    The battle rages all around you. You see comrades fall with limbs hanging loose. A screaming 
    daamon hurls itself at you. What do you do?
    """)
    time.sleep(2)
    print("""
    [A] Attack 
    [F] Fall back to the nearest squad
    [D] Drop your weapon and shit your pants
    """)
    while True:
        choice = input("").upper()
        if choice == "A":
            soldierA1(hero)
        elif choice == "F":
            soldierA2(hero)
        elif choice == "D":
            soldierA3(hero)
        else:
            print("Invalid choice.")
            continue


def soldierA1(hero):
    daamon = characters.Daamon("Daamon")
    game.combat(hero, daamon)
    game.menu(hero)
    print("""
    You fell the beast before you. The stench of death fills your nostrils and the screams of the dying
    invade your ears. The tide of the battle appears to be turning. You can almost feel the pressure
    building behind you, forcing you forward to continue the assualt...    
    """)
    time.sleep(2)
    soldierB1(hero, "a1")


def soldierA2(hero):
    print("""
    You fall back to the nearest squad. Together you engage the daamon and overwhelm it. The momentum of
    battle continues to push you forward 
    """)
    time.sleep(2)
    soldierB1(hero, "a2")


def soldierA3(hero):
    print("""
    You are overcome with fear. You loose all feeling in your fingers and drop you weapon. You close your 
    eyes.The daamon raises its weapon to deliver a killing blow...
    """)
    time.sleep(2)
    print("""You open your eyes to see a majestic, armoured Being gallop past on what can only be described
    as a giant horse. The Being gracefully severs the daamon's head with one swing and proceeds to charge
    into the next group of enemies. 
    """)
    time.sleep(1)
    print("""
    You stare in disbelief - your head is still attached to your body! You fall to you knees and begin
    to sob into your hands...
    """)
    time.sleep(2)
    soldierB1(hero, "a3")


def soldierB1(hero, choice):


def soldierB2(hero):
    print("""
    You cannot contain the simmering rage which has just gripped your heart. You get up and 
    stride towards the sergeant. 'Hoi Sir, you forgot something!'
    """)
    time.sleep(2)
    sergeant = characters.Military_Human("Sergeant")
    game.combat(hero, sergeant)
    game.menu(hero)
    pass
    #TODO: test this fight


def soldierB3(ero):
    pass

def soldierB4(hero):
    pass



