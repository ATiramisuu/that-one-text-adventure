import saveProgress


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




def startGame():
    print("New game started!\n")
    startArea()


def startArea():
    name = input("Enter your name: ")
    game_state = {"name": name}
    saveProgress.save_game(game_state)
    print("Hello " + name)

    readScript(1, 10)

    while True:
        option = input("What would you like to do? ")

        if option == "1":
            readScript(10, 16)

        elif option == "2":
            readScript(21, 30)

        elif option == "3":
            readScript(31, 40)
            break

        else: 
            print("Invalid input! Select a valid option.")




def continueArea(game_state):
    print("Continuing game with previous save data \nWelcome back" + game_state['name'])
