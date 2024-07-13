import os
from game_classes import GameState
import firstArea


print("Welcome to That One Text Adventure")

def menu():
    print("\nPlease choose 1 of the following options:",
          "1. Start new game",
          "2. Continue game",
          "3. Exit", sep="\n", end="\n\n")

# -------------------------------------------------------------------------------------

def main():
    while True:
        menu()
        game_state = GameState.load()
        try:
            option = input("Select option to start: ")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if option == "1":
            if game_state:
                wipe = input("Existing save data found. Do you want to wipe the data and start over? (yes/no): ").strip().lower()
                if wipe == "yes":
                    try:
                        os.remove("saveData.txt")
                        GameState.reset_json_files()
                        print("Save data wiped and inventories reset. Starting a new game!")
                        firstArea.startGame()
                        break
                    except FileNotFoundError:
                        print("No save file found. Starting a new game!")
                        GameState.reset_json_files()
                        firstArea.startGame()
                        break
                else:
                    print("Okay, going back to the main menu now.")
            else:
                print("Starting a new game!")
                GameState.reset_json_files()
                firstArea.startGame()
                break

        elif option == "2":
            if not game_state:
                print("You haven't started a new game or no save data found! Please start a new game first.")
            else:
                print("Finding save file...")
                print("Save file found! Continuing your game")
                firstArea.continueArea(game_state)
                break

        elif option == "3":
            print("Exiting the program now")
            exit(1)
        else:
            print("Your input is invalid, please try again")

if __name__ == "__main__":
    main()

