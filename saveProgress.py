def save_game(state):
  with open("saveData.txt", "w") as file:
      file.write(state["name"])


def load_game():
  try:
      with open("saveData.txt", "r") as file:
          content = file.read()

          if not content: # we check if the file is empty
              return None

          return {"name": content}

  except FileNotFoundError:
      return None
