import json


class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


# -------------------------------------------------------------------------------------

class Inventory:
    def __init__(self, items, balance=0):
        self.items = [Item(**item) for item in items]
        self.balance = balance


    def add_item(self, item_name, amount):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.amount += amount
                return
        # If item not found, add new item
        new_item = next((item for item in self.items if item.name.lower() == item_name.lower()), None)
        if new_item:
            self.items.append(Item(item_name, new_item.price, amount))


    def remove_item(self, item_name, amount):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                if item.amount >= amount:
                    item.amount -= amount
                    return True
        return False


    def get_item(self, item_name):
        return next((item for item in self.items if item.name.lower() == item_name.lower()), None)


# -------------------------------------------------------------------------------------

class Store:
    def __init__(self, inventory_file):
        self.inventory = self.load_inventory(inventory_file)

    def load_inventory(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return Inventory(data['items'])

    def save_inventory(self, file_name):
        data = {
            'items': [{'name': item.name, 'price': item.price, 'amount': item.amount} for item in self.inventory.items]
        }
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)


# -------------------------------------------------------------------------------------

class Player:
    def __init__(self, name, inventory_file):
        self.name = name
        self.inventory = self.load_inventory(inventory_file)

    def load_inventory(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return Inventory(data['items'], data['balance'])

    def save_inventory(self, file_name):
        data = {
            'balance': self.inventory.balance,
            'items': [{'name': item.name, 'price': item.price, 'amount': item.amount} for item in self.inventory.items]
        }
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)


# -------------------------------------------------------------------------------------

class GameState:
    def __init__(self, player_name):
        self.player_name = player_name


    def save(self):
        with open("saveData.txt", "w") as file:
            file.write(self.player_name)


    @classmethod
    def load(cls):
        try:
            with open("saveData.txt", "r") as file:
                content = file.read()
                if not content:
                    return None
                return cls(content)
        except FileNotFoundError:
            return None


    @staticmethod
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

