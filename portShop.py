import json

def welcomeShop():  # Print out the welcome message and start the store inventory process
    print("You've entered the general store! Welcome!")
    shop_for_supplies()


def load_store_inventory():  # get the current store inventory from the json file
    try:
        with open("storeInventory.json", "r") as file:
            inventory = json.load(file)
        return inventory
    except Exception as e:
        print(f"An error occurred while loading the store inventory: {e}")
        return None


def save_store_inventory(inventory):
    try:
        with open("storeInventory.json", "w") as file:
            json.dump(inventory, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the store inventory: {e}")


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

    if storeInventory and shipInventory:  # if we load both the store and ship inventory successfully
        while True:  # loop until the user chooses to exit
            print("\n")
            print("- " * 40)  # make it easier to read

            display_inventory(storeInventory, "General Store")  # display the store inventory
            print("\nYou currently have " + str(shipInventory['balance']) + " gold coins.")
            itemName = input("\nEnter item name (or 'exit' to leave the store): ").strip().lower()

            if itemName == 'exit':
                print("Okay, leaving the general store now!")
                break

            # Check if the entered item name is in the store inventory
            itemFound = None  # we assume no item found yet
            for item in storeInventory["items"]:
                if item["name"].strip().lower() == itemName:  # this option will be for a valid item name
                    itemFound = item  # we found the item
                    break

            if itemFound:  # if we found the item
                print("I got the input: " + itemName)
                try:  # we're now going to try to buy x number of the item
                    amount = int(input("\nHow much " + itemName + " do you want to buy? ").strip())

                    # check if the user wants 0 or less items
                    if amount <= 0:
                        print("Invalid amount. Please enter a positive number.")
                        continue
                    
                    # check if the user wants more than is currently in stock
                    if amount > itemFound["amount"]:
                        print("Sorry, we only have " + str(itemFound["amount"]) + " of " + itemName + " in stock.")
                        continue
                
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue

                # we're going to get the total cost of their purchase
                totalCost = amount * itemFound['price']
                print("Buying " + str(amount) + " " + itemName + " will cost you " + str(totalCost) + " gold coins.")
                print("You currently have " + str(shipInventory['balance']) + " gold coins.")

                # we're now going to ask the user to confirm the purchase
                confirm = input("\nConfirm purchase? (yes/no) ").strip().lower()
                if confirm == "yes":
                    if totalCost <= shipInventory["balance"]:  # if we have enough gold coins
                        print("Okay, we'll buy " + str(amount) + " " + itemName + "!")

                        # Update ship inventory
                        itemNameInShip = None
                        for ship_item in shipInventory["items"]:
                            if ship_item["name"].strip().lower() == itemName:
                                itemNameInShip = ship_item
                                break

                        if itemNameInShip:  # if we can find that item type in our ship inventory
                            itemNameInShip["amount"] += amount  # we add the amount to the existing amount
                        else:  # if the item is not found, add it to the ship inventory
                            shipInventory["items"].append({"name": itemName, "amount": amount})

                        itemFound["amount"] -= amount # update store inventory
                        shipInventory["balance"] -= totalCost # update balance

                        save_ship_inventory(shipInventory) # save ship inventory
                        save_store_inventory(storeInventory) # save store inventory

                        print("Subtracting " + str(totalCost) + " from your balance!")  # display the amount subtracted from the balance
                        print("Purchase successful!")  # purchase success message
                        print("You now have " + str(shipInventory['balance']) + " gold coins!")  # display new gold coin balance

                        display_inventory(storeInventory, "Updated Store")
                        display_inventory(shipInventory, "Updated Ship")

                    else:  # if we don't have enough gold coins
                        print("Sorry, you don't have enough gold coins to buy " + str(amount) + " " + itemName + ".")

                    # regardless of which branch we take, we're going to print this line & continue the while loop
                    print("Going back to the main general store...")

                else:  # if there's any other input (user denies purchase)
                    print("Okay, we won't buy " + str(amount) + " " + itemName + "!")
                    print("Going back to the main general store...")

            else:  # otherwise, invalid input
                print("Invalid input! Please enter a valid item name.")

