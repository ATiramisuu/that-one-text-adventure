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
    # we load store inventory or initialize if not found
    storeInventory = load_store_inventory()
    if storeInventory is None:
        print("Failed to load store inventory. Exiting.")
        return
    
    # we load ship inventory or initialize if not found
    shipInventory = load_ship_inventory()
    if shipInventory is None:
        print("Failed to load or initialize ship inventory. Exiting.")
        return

    if storeInventory and shipInventory: # if we load both the store and ship inventory successfully
        while True: # loop until the user chooses to exit
            print("\n")
            print("- " * 40) # make it easier to read
            
            display_inventory(storeInventory, "General Store") # display the store inventory
            print("\nYou currently have " + str(shipInventory['balance']) + " gold coins.")
            itemName = input("\nEnter the name of the item you want to buy (or 'exit' to leave the store): ").strip().lower()
            if itemName == 'exit':
                print("Okay, leaving the general store now!")
                break

            else: # any other input
                #print("I got the input: " + itemName)
                found = False # we assume the itemName is not found
                for item in storeInventory["items"]: # loop through the store inventory
                    if item["name"].strip().lower() == itemName: # if we find the item
                        found = True # we set found to True
                        
                        try: # we're now going to try to buy x number of the item
                            amount = int(input("\nHow many " + itemName + " do you want to buy? ").strip())
                            
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                            continue

                        totalCost = amount * item['price']
                        print("Buying " + str(amount) + " " + itemName + " will cost you " + str(totalCost) + " gold coins.")
                        print("You currently have " + str(shipInventory['balance']) + " gold coins.")
                        break
