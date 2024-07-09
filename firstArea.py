import saveProgress

def startArea():
    weapon = input("enter the name of your weapon: ")
    game_state =  {"weapon": weapon}
    saveProgress.save_game(game_state)
    print("Selected Weapon: " + weapon)


def continueArea():
    game_state = saveProgress.load_game()
    if game_state:
        print("Continuing game with previous save data \n Current weapon: " + game_state['weapon'])
    else:
        print("No save game found \n Starting new game")
        startArea()



def startGame():
    print("game started")