import characters

def main():
    hero = characters.Hero("Bjorn", "Warrior")
    print(hero.get_details())
    print(hero.get_attributes())
    print(hero.get_inventory())




if __name__ == "__main__":
    main()