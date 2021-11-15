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
            soldierA2()
        elif choice == "D":
            soldierA3()
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
    soldierB1()


def soldierA2():
    print("""
    You fall back to the nearest squad. Together you engage the daamon and overwhelm it. The momentum of
    battle continues to push you forward 
    """)
    time.sleep(2)
    soldierB1()


def soldierA3():
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


def soldierB1():
    print("""
        It takes the better part of the night for the enemy to finally turn and flee. Tonight there will be
        time for some sombre celebrations...
        """)
