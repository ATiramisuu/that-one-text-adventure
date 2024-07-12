import json


# this makes sure that our json files are getting created and reset properly each time we start a new game
def reset_json_files():
    store_inventory = {
        "items": [
            {"name": "rum", "price": 15, "amount": 24},
            {"name": "bread", "price": 5, "amount": 50},
            {"name": "rope", "price": 20, "amount": 10}
        ]
    }

    ship_inventory = {
        "balance": 500,
        "items": [
            {"name": "rum", "price": 15, "amount": 0},
            {"name": "bread", "price": 5, "amount": 0},
            {"name": "rope", "price": 20, "amount": 0}
        ]
    }

    with open("storeInventory.json", "w") as file:
        json.dump(store_inventory, file, indent=4)

    with open("shipInventory.json", "w") as file:
        json.dump(ship_inventory, file, indent=4)



# this makes sure our saveData.txt file is getting saved each time
def save_game(state):
  with open("saveData.txt", "w") as file:
      file.write(state["name"])


# this makes sure our saveData.txt file is getting loaded each time
def load_game():
  try:
      with open("saveData.txt", "r") as file:
          content = file.read()

          if not content: # we check if the file is empty
              return None

          return {"name": content}

  except FileNotFoundError:
      return None
