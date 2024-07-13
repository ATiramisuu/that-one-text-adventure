from game_classes import Store, Player


def welcomeShop():
    print("You've entered the general store! Welcome!")
    shop_for_supplies()

# -------------------------------------------------------------------------------------

def shop_for_supplies():
    store = Store("storeInventory.json")
    player = Player("Player", "shipInventory.json")

    while True:
        print("\n" + "-" * 40)
        display_inventory(store.inventory, "General Store")
        print(f"\nYou currently have {player.inventory.balance} gold coins.")

        item_name = input("\nEnter item name (or 'exit' to leave the store): ").strip().lower()

        if item_name == 'exit':
            print("Okay, leaving the general store now!")
            break

        item = store.inventory.get_item(item_name)
        if item:
            try:
                amount = int(input(f"\nHow much {item_name} do you want to buy? ").strip())
                if amount <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue
                if amount > item.amount:
                    print(f"Sorry, we only have {item.amount} of {item_name} in stock.")
                    continue

                total_cost = amount * item.price
                print(f"Buying {amount} {item_name} will cost you {total_cost} gold coins.")
                print(f"You currently have {player.inventory.balance} gold coins.")

                confirm = input("\nConfirm purchase? (yes/no) ").strip().lower()
                if confirm == "yes":
                    if total_cost <= player.inventory.balance:
                        store.inventory.remove_item(item_name, amount)
                        player.inventory.add_item(item_name, amount)
                        player.inventory.balance -= total_cost

                        store.save_inventory("storeInventory.json")
                        player.save_inventory("shipInventory.json")

                        print(f"Purchase successful! You now have {player.inventory.balance} gold coins!")
                        display_inventory(store.inventory, "Updated Store")
                        display_inventory(player.inventory, "Updated Ship")
                    else:
                        print(f"Sorry, you don't have enough gold coins to buy {amount} {item_name}.")
                else:
                    print(f"Okay, we won't buy {amount} {item_name}!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid input! Please enter a valid item name.")

# -------------------------------------------------------------------------------------

def display_inventory(inventory, title):
    print(f"\n{title} Inventory:\n")
    for item in inventory.items:
        print(f"Item: {item.name}, Price: {item.price}, Amount: {item.amount}")

