import firstArea
import saveProgress
import os

print("Welcome to That One Text Adventure")  # Welcome the player to your game --> non-repeatable line


def menu():  # Create a menu with different options
    print("\nPlease choose 1 of the following options:",
          "1. Start new game",
          "2. Continue game",
          "3. Exit", sep="\n", end="\n\n")


def main():
    while True:
        menu()  # Run the menu function
        game_state = saveProgress.load_game()

        try:
            option = input("Select option to start: ")
        except ValueError:  # If we get a ValueError from invalid input
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if option == "1":  # We want to start a new game
            if game_state:  # Check if there is existing save data
                wipe = input("Existing save data found. Do you want to wipe the data and start over? (yes/no): ").strip().lower()
                if wipe == "yes":
                    try:     
                        os.remove("saveData.txt")
                        saveProgress.reset_json_files()  # Reset JSON files
                        print("Save data wiped and inventories reset. Starting a new game!")
                        firstArea.startGame()
                        break # Exit the while loop
                        
                    except FileNotFoundError: 
                        print("No save file found. Starting a new game!")
                        saveProgress.reset_json_files()  # Reset JSON files anyway
                        firstArea.startGame()
                        break
                else:
                    print("Okay, going back to the main menu now.")  # you'll get booted back out to the main menu
            else:
                print("Starting a new game!")  # This starts a new game
                saveProgress.reset_json_files()  # Reset JSON files for a new game
                firstArea.startGame()
                break  # Exit the while loop

        elif option == "2":  # We want to continue our game
            if not game_state:  # We haven't started a new game yet or save file is empty
                print("You haven't started a new game or no save data found! Please start a new game first.")
            else:  # We have already started a new game
                print("Finding save file...")
                print("Save file found! Continuing your game")
                firstArea.continueArea(game_state)
                break  # Exit the while loop

        elif option == "3":  # We want to exit the program
            print("Exiting the program now")
            exit(1)

        else:  # Our user input is invalid
            print("Your input is invalid, please try again")


if __name__ == "__main__":
    main()
