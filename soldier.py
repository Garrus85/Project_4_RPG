import characters
import time
import game

def story(hero):
    print(hero.get_details())
    #print(hero.level)
    time.sleep(1)

    print("""
    The battle rages all around you. You see comrades fall on either side of you. A screaming daamon hurls itself
    at you. What do you do?
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
            soldierA2()
        elif choice == "D":
            soldierA3()
        else:
            print("Invalid choice.")
            continue


def soldierA1(hero):
    daamon = characters.Daamon("Daamon")
    game.combat(hero, daamon)


def soldierA2():
    pass


def soldierA3():
    pass

