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
            soldier_a1(hero)
        elif choice == "F":
            soldier_a2(hero)
        elif choice == "D":
            soldier_a3(hero)
        else:
            print("Invalid choice.")
            continue


def soldier_a1(hero):
    daamon = characters.Daamon("Daamon")
    game.combat(hero, daamon)
    game.menu(hero)
    print("""
    You fell the beast before you. The stench of death fills your nostrils and the screams of the dying
    invade your ears. The tide of the battle appears to be turning. You can almost feel the pressure
    building behind you, forcing you forward to continue the assualt...    
    """)
    time.sleep(2)
    soldier_b1(hero, "a1")


def soldier_a2(hero):
    print("""
    You fall back to the nearest squad. Together you engage the daamon and overwhelm it. The momentum of
    battle continues to push you forward 
    """)
    time.sleep(2)
    soldier_b1(hero, "a2")


def soldier_a3(hero):
    print("""
    You are overcome with fear. You loose all feeling in your fingers and drop you weapon. You close your 
    eyes.The daamon raises its weapon to deliver a killing blow...
    """)
    time.sleep(2)
    print("""
    You open your eyes to see a majestic, armoured Being gallop past on what can only be described
    as a giant horse. The Being gracefully severs the daamon's head with one swing and proceeds to charge
    into the next group of enemies. 
    """)
    time.sleep(1)
    print("""
    You stare in disbelief - your head is still attached to your body! You fall to you knees and begin
    to sob into your hands...
    """)
    time.sleep(2)
    soldier_b1(hero, "a3")


def soldier_b1(hero, choice):
    print(""" 
    You stare into the flames, sipping on your drink which tastes somewhere between rum and horseshit. 
    The crackle from the fire is accompanied by the low murmurs of subdued, battleworn soldiers. The
    crunching of boots on gravel announces your sergeants arrival.
    """)
    time.sleep(2)
    #TODO: recreate the sergeants conversation
    if choice == "a1":
        print("""
        'I heard you stood your ground and took down one of those bastards by yourself. If only all of 
        our men had your stubborn stupidity, hah.'
        You grunt in response. The sergeant just stares at you, probably expecting some sort of heroic 
        response.
        """)
    elif choice == "a2":
        print("""
        Saw you managed to keep yer wits about you in the heat of battle. Better to fall back, strength in
        numbers an' all that! Rather that then get yer skull smashed in!'
        The sergeant looks around at the surrounding camp fires.
        """)
    else:
        pass
    time.sleep(2)
    print("""
        'Anyways, Cap'n send me to tell you that yer brother is on the run. He's a filthy Twilight Adept
        and was sentenced to execution before he slipped his chains and disappeared. Thought you'd want to
        know.'
        He continues to stare at you, with a slight smirk on his face. You sit there, unable to fully
        comprehend what he just said.
        'I'll be keeping an eye on you. Evil breeds evil so the first sign of you showing any affinity to
        power and I'll 'av your head! Hah'
        The sergeant spins on his heels and begins walking back the way he had come. 
        """)
    time.sleep(2)
    while True:
        print("""
        [A] Continue to sit and stare into the fire.
        [B] Go and rearrange the sergeants face.
        [C] Return to your tent and prepare to leave.
        """)
        choice = input().upper()
        if choice == "A":
            soldier_b2(hero)
        elif choice == "B":
            soldier_b3(hero)
        elif choice == "C":
            soldier_b4(hero)
        else:
            print("Invalid choice.")
            continue

def soldier_b2(hero):
    pass

def soldier_b3(hero):
    print("""
    You cannot contain the simmering rage which has just gripped your heart. You get up and 
    stride towards the sergeant. 
    'Hoi Sir, you forgot something!'
    """)
    time.sleep(2)
    sergeant = characters.Military_Human("Sergeant")
    game.combat(hero, sergeant)
    game.menu(hero)


def soldier_b3(hero):
    pass


def soldier_b4(hero):
    pass



