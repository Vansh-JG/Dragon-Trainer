import check_input
from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
import random

def main():
    name = input("What is your name, challenger? ")
    hero = Hero(name, 50)
    dragons = [Dragon("Deadly Nadder", 10), FireDragon("Gronckle", 15, 3), FlyingDragon("Timberjack", 20, 5)]
    # name = input("What is your name, challenger? ")
    print("Welcome to dragon training, " + name)
    print("You must defeat 3 dragons.")
    print("")

    while hero.hp > 0 or len(dragons) > 0:
        print()
        print(f'{hero.name} : {hero.hp}/{hero._max_hp}')
        for i in range(len(dragons)):
            print(f"{str(i + 1)}. Attack {dragons[i].name} : {dragons[i].hp}/{dragons[i]._max_hp}")
            if dragons[i].name == "Gronckle":
                print(dragons[i].__str__())
            elif dragons[i].name == "Timberjack":
                print(dragons[i].__str__())

        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
        print()
        print("Attack with:")
        print("1. Sword (2 D6)")
        print("2. Arrow (1 D12)")
        weapon = check_input.get_int_range("Enter weapon: ", 1, 2)
        print()
        if dragon_choice == 1 and weapon == 1:
            print(hero.basic_attack(dragons[0]))
        elif dragon_choice == 1 and weapon == 2:
            print(hero.special_attack(dragons[0]))
        elif dragon_choice == 2 and weapon == 1:
            print(hero.basic_attack(dragons[1]))
        elif dragon_choice == 2 and weapon == 2:
            print(hero.special_attack(dragons[1]))
        elif dragon_choice == 3 and weapon == 1:
            print(hero.basic_attack(dragons[2]))
        elif dragon_choice == 3 and weapon == 2:
            print(hero.special_attack(dragons[2]))

        dragon = dragons[dragon_choice - 1]
        if dragon.hp <= 0:
            dragons.pop(dragon_choice - 1)
            print(f"")

        if len(dragons) == 0:
            print()
            print("Congratulations! You have defeated all 3 dragons, you have passed the trials.")
            break
        elif hero.hp <= 0:
            print("You have been defeated." + "\n" + "Game over")
            break
        else:
            damage_drag = random.choice(dragons)
            damage = random.randint(1, 2)
            if damage == 1:
                print(damage_drag.basic_attack(hero))
            elif damage == 2:
                print(damage_drag.special_attack(hero))


main()