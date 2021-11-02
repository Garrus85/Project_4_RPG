import characters
import game
import soldier
import rogue
import adept


def main():
    name, role = game.intro()
    hero = characters.Hero(name, role)
    #print(hero.get_details())

    if role == "S":
        soldier.story(hero)
    elif role == "R":
        rogue.story(hero)
    else:
        adept.story(hero)

   # print(hero.get_inventory())




if __name__ == "__main__":
    main()