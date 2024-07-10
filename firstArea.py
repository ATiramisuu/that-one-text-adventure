import saveProgress


def startGame():
    print("New game started!\n")
    startArea()


def startArea():
    weapon = input("Enter the name of your weapon: ")
    game_state = {"weapon": weapon}
    saveProgress.save_game(game_state)
    print("Selected Weapon: " + weapon)


def continueArea(game_state):
    print("Continuing game with previous save data \nCurrent weapon: " + game_state['weapon'])
