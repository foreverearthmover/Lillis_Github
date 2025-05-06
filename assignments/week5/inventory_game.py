# --- Game State ---
inventory = []
items_in_room = [
    {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
    {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
    {"name": "Key", "type": "tool", "description": "Opens a locked door."}
] # length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    pass

def show_room_items():
    # list all items in current room
    pass

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet, removed from room inv
    pass

def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    pass

def use(item_name):
    # Ex: use the item differently depends on the type
    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    pass

# --- Game Loop ---

def game_loop():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
