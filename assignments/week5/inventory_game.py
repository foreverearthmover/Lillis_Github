#

inventory = []
MAX_INVENTORY_SIZE = 5
items_in_room = []

rooms = {
    "room1": {
        "description": "A dimly lit room. You sense something hidden.",
        "items": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "Cat Treats", "type": "quest", "description": "Smells like tuna. A cat might like these."}
        ],
        "next": "room2"
    },
    "room2": {
        "description": "A room with ancient runes and glowing artifacts.",
        "items": [
            {"name": "Rune Stone", "type": "quest", "description": "Glows faintly."},
            {"name": "Ancient Coin", "type": "quest", "description": "Stamped with a cat's face."},
            {"name": "Crystal Shard", "type": "quest", "description": "Feels warm in your hand."}
        ],
        "next": "room3"
    },
    "room3": {
        "description": "A grand hall. A gigantic cat blocks your path.",
        "items": [
            {"name": "Mystic Dagger", "type": "weapon", "description": "Gleams with ancient energy. Could it defeat the cat?"}
        ],
        "next": None
    }
}

#tracks current room
current_room = "room1"

# --- Functions ---

def prompt():
    print("\tWelcome to my game!\n\n"
          "Explore the rooms to escape this dungeon.\n"
          "Type help for a list of commands.\n")

    input("Press Enter to continue...")

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if inventory:
        print("Inventory:")
        for item in inventory:
            print(f"- {item['name']}")
    else:
        print("You don't have any items in your inventory.")

def show_room_items():
    # list all items in current room
    room = rooms[current_room]
    print(f"\nYou are in the {current_room} room. {room[description]}")
    if room["items"]:
        print("You see:")
        for item in room["items"]:
            print(f"- {item['name']}")
    else:
        print("There are no items here.")

def find_item(item_name, item_list):
    return next((item for item in item_list if item["name"].lower() == item_name.lower()), None)

def pick_up(item_name):
    global inventory
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full. You can't pick up any more items.")
        return
    item = find_item(item_name, rooms[current_room]["items"])
    if item:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        print(f"You picked up a {item['name']}.")
    else:
        print(f"There is no item called {item_name} here.")
    # pick up an item from the room if inventory limit is not met yet, removed from room inv


def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    global inventory
    item = find_item((item_name, inventory))
    if item:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        print(f"You dropped a {item['name']}.")
    else:
        print(f"You don't have a {item_name} in your inventory.")

def use(item_name):
    # Ex: use the item differently depends on the type
    global current_room
    item = find_item(item_name, inventory)
    if not item:
        print(f"You don't have a {item_name} in your inventory.")
        return

    if item['type'] == "food":
        print(f"You eat the {item['name']}. It was tasty.")
        inventory.remove(item)
    elif item['type'] == "weapon" and current_room == "room3":
        print("You raise the Mystic Dagger to strike the cat...")
        print("But before you do, the cat speaks!")
        print("\n'Why did you try to attack me? I was sentient all along.'")
        print("The cat vanishes. Your game ends in regret. You're locked out forever.\n")
        exit()
    elif item['type'] == "quest" and item['name'] == "Cat Treats" and current_room == "room3":
        print("You offer the Cat Treats. The cat purrs and allows you to pass.")
        print("You've completed the game peacefully. Well done!")
        exit()
    else:
        print(f"You can't use the {item['name']} here.")

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    item = find_item(item_name, inventory) or find_item(item_name, rooms[current_room]["items"])
    if item:
        print(f"You examine the {item['name']}.")
        print(item["description"])
    else:
        print(f"There is no {item_name} here.")

def try_next_room():
    global current_room
    if current_room == "room1":
        current_room = "room2"
        print("You proceed to the next room.")
    elif current_room == "room2":
        required = {"Rune Stone", "Ancient Coin", "Crystal Shard"}
        if required.issubset(set(item["name"] for item in inventory)):
            current_room = "room3"
            print("The magical door opens as you gold the three items")
        else:
            print("You can't go further. You need to find the required items.")

    elif current_room == "room3":
        print("The cat blocks your path. You can't go further if you don't use or offer something to interact.")

# --- Game Loop ---

def game_loop():
    prompt()
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
