import random
import characters
import game
import soldier


# --------TESTS-------
hero = characters.Hero("Bjorn", "S")
#soldier.soldierB2(hero)
soldier.soldier_b1(hero, "a3")

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
