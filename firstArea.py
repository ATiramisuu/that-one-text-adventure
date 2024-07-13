from game_classes import GameState, Player
import portShop


def readScript(start_line, end_line):
    try:
        with open("portScript.txt", 'r') as file:
            lines = file.readlines()
            specific_lines = lines[start_line - 1:end_line]
            for line in specific_lines:
                print(line.strip())
            print("- " * 40)  
    except Exception as e:
        print(f"An error occurred: {e}")

# -------------------------------------------------------------------------------------

def startGame():
    print("New game started!\n")
    name = input("Enter your name: ")
    game_state = GameState(name)
    game_state.save()
    print("Hello " + name)
    startArea()

# -------------------------------------------------------------------------------------

def startArea():
    readScript(1, 6)
    while True:
        readScript(6, 10)
        option = input("\nWhat would you like to do? ")
        if option == "1":
            readScript(10, 16)
        elif option == "2":
            print("Let's go to the general store!\n")
            portShop.welcomeShop()
            break
        elif option == "3":
            readScript(31, 40)
            break
        else: 
            print("Invalid input! Select a valid option.")

# -------------------------------------------------------------------------------------

def continueArea(game_state):
    print("\nContinuing game with previous save data \nWelcome back " + game_state.player_name)
    startArea()

