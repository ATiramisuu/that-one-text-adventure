def save_game(state):
    with open("saveData.txt", "w") as file:
        file.write(state["weapon"])


def load_game():
    try:
        with open("saveData.txt", "r") as file:
            weapon = file.read()
            return {"weapon": weapon}
    except FileNotFoundError:
        return None
