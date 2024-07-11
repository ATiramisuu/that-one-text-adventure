import json


def welcomeShop():  # Print out the welcome message and start the store inventory process
    print("You've entered the general store! Welcome!")
    shop_for_supplies()


  def load_store_inventory(): # get the current store inventory from the json file
  try:
      with open("storeInventory.json", "r") as file:
          inventory = json.load(file)
      return inventory

  except Exception as e:
      print(f"An error occurred while loading the store inventory: {e}")
      return None


def display_inventory(inventory, title):
    print("\n" + title + " Inventory:\n")
    for item in inventory["items"]:
        print("Item: " + item['name'] +
              ", Price: " + str(item['price']) +
              ", Amount: " + str(item['amount'])
             )


def load_ship_inventory():
    try:
        with open("shipInventory.json", "r") as file:
            inventory = json.load(file)
        return inventory
    except Exception as e:
        print(f"An error occurred while loading the ship inventory: {e}")
        return None


def save_ship_inventory(inventory):
    try:
        with open("shipInventory.json", "w") as file:
            json.dump(inventory, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the ship inventory: {e}")


def shop_for_supplies():
    storeInventory = load_store_inventory()
    shipInventory = load_ship_inventory()

    if storeInventory and shipInventory: # if we load both the store and ship inventory successfully
        while True: # loop until the user chooses to exit
            display_inventory(storeInventory, "General Store") # display the store inventory
            itemName = input("\nEnter the name of the item you want to buy (or 'exit' to leave the store): ").strip().lower()
            if itemName == 'exit':
                print("Okay, leaving the general store now!")
                break

            else: # any other input
                print("I got the input: " + itemName)
                break
