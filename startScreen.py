

def menu():
    print("Welcome to That One Text Adventure")
    print("1. Start New Game")
    print("2. Continue Game")
    print("3. Exit Game")
    

def main():
    menu()
    option = int(input("select option to start: "))
    if option == 1:
        print("New Game Started")
        import firstArea
        firstArea.startGame()
    elif option == 2:
        print("Finding Game file...")

    elif option == 3:
        print("Exiting Game")
        exit(1)

main()
