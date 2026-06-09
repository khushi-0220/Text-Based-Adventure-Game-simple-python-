# ========================================
#   TEXT-BASED ADVENTURE GAME
#   Author: Khushi
# ========================================

def display_banner():
    print("==========================================")
    print("        THE LOST KINGDOM                  ")
    print("        A Text Adventure Game             ")
    print("        Author: Khushi                    ")
    print("==========================================")
    print()


def get_choice(options):
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice! Please enter one of: " + ", ".join(options))


def show_inventory(inventory):
    print("\n--- INVENTORY ---")
    if inventory:
        for item in inventory:
            print("  - " + item)
    else:
        print("  (empty)")
    print()


def start_game():
    display_banner()
    print("Welcome, brave adventurer!")
    print("A dark curse has fallen upon the Lost Kingdom.")
    print("Only a true hero can lift it.")
    print()
    name = input("Enter your name: ").strip()
    if not name:
        name = "Hero"
    print()
    print("Welcome, " + name + "! Your quest begins now...")
    print()
    return name


def forest_path(name, inventory):
    print("------------------------------------------")
    print("SCENE 1: The Dark Forest")
    print("------------------------------------------")
    print("You stand at the edge of a dark forest.")
    print("Two paths stretch before you:")
    print("  [1] Take the left path (towards a glowing light)")
    print("  [2] Take the right path (towards strange sounds)")
    print("  [3] Check your inventory")

    choice = get_choice(["1", "2", "3"])

    if choice == "3":
        show_inventory(inventory)
        return forest_path(name, inventory)

    elif choice == "1":
        print()
        print("You follow the glowing light and find a friendly fairy!")
        print("The fairy gives you a MAGIC SWORD and vanishes.")
        inventory.append("Magic Sword")
        print(">> Magic Sword added to inventory!")
        print()
        return cave_entrance(name, inventory)

    elif choice == "2":
        print()
        print("You encounter a pack of wolves blocking the path!")
        print("What do you do?")
        print("  [a] Fight the wolves")
        print("  [b] Run back to the forest entrance")
        fight = get_choice(["a", "b"])
        if fight == "a":
            if "Magic Sword" in inventory:
                print()
                print("You slash through with your Magic Sword and defeat the wolves!")
                return cave_entrance(name, inventory)
            else:
                print()
                print("You have no weapon! The wolves overwhelm you...")
                return game_over(name)
        else:
            print()
            print("You sprint back and find another route through the forest.")
            return cave_entrance(name, inventory)


def cave_entrance(name, inventory):
    print("------------------------------------------")
    print("SCENE 2: The Cave")
    print("------------------------------------------")
    print("You arrive at the entrance of a dark cave.")
    print("A riddle is carved into the stone wall:")
    print()
    print("  'I have cities, but no houses live there.")
    print("   I have mountains, but no trees grow there.")
    print("   I have water, but no fish swim there.")
    print("   What am I?'")
    print()
    print("  [1] Answer: A Map")
    print("  [2] Answer: A Dream")
    print("  [3] Answer: A Cloud")

    choice = get_choice(["1", "2", "3"])

    if choice == "1":
        print()
        print("CORRECT! The cave door rumbles open!")
        print()
        return final_battle(name, inventory)
    else:
        print()
        print("Wrong answer! Try the riddle again.")
        return cave_entrance(name, inventory)


def final_battle(name, inventory):
    print("------------------------------------------")
    print("SCENE 3: The Final Battle")
    print("------------------------------------------")
    print("Inside the cave, you face the DARK SORCERER!")
    print('"So, ' + name + '... you dare challenge me?!" he roars.')
    print()
    print("How will you fight him?")
    print("  [1] Attack with your weapon")
    print("  [2] Use a magic spell")
    print("  [3] Try to negotiate")

    choice = get_choice(["1", "2", "3"])

    if choice == "1":
        if "Magic Sword" in inventory:
            print()
            print("You charge forward with your Magic Sword!")
            print("The sorcerer is defeated! The curse is broken!")
            return victory(name)
        else:
            print()
            print("Your bare hands are no match for dark magic!")
            return game_over(name)

    elif choice == "2":
        print()
        print("You don't know any spells! The sorcerer blasts you away.")
        return game_over(name)

    elif choice == "3":
        print()
        print("'Wait!' you say. 'What do you actually want?'")
        print("The sorcerer pauses. 'I just want... a friend.'")
        print("You offer to visit him every week. He lifts the curse!")
        print("Peace is restored through kindness!")
        return victory(name)


def game_over(name):
    print()
    print("==========================================")
    print("              GAME OVER                   ")
    print("==========================================")
    print(name + "'s adventure ends here...")
    print("But every hero gets another chance!")
    print()
    print("  [r] Restart   [q] Quit")
    choice = get_choice(["r", "q"])
    if choice == "r":
        main()
    else:
        print()
        print("Thanks for playing! - Khushi")


def victory(name):
    print()
    print("==========================================")
    print("              YOU WIN!                    ")
    print("==========================================")
    print("Congratulations, " + name + "!")
    print("You have saved the Lost Kingdom!")
    print("The people cheer your name as a legend.")
    print()
    print("         *** THE END ***")
    print()
    print("Thanks for playing! - Author: Khushi")
    print()
    print("  [r] Play Again   [q] Quit")
    choice = get_choice(["r", "q"])
    if choice == "r":
        main()
    else:
        print()
        print("Farewell, adventurer! - Khushi")


def main():
    inventory = []
    name = start_game()
    forest_path(name, inventory)


main()