# This is a dungeon escape game.
# You need to complete quests by picking up items to make it to the end.

inventory = []
MAX_INVENTORY_SIZE = 5
items_in_room = []

rooms = {
    "first room": {
        "description": "A dimly lit room. You sense something hidden.",
        "items": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "Treats", "type": "quest", "description": "Smells like tuna. A cat might like these."}
        ],
        "next": "second room"
    },
    "second room": {
        "description": "It looks kinda magical in here... There's all kinds of embellished objects just laying"
                       "\naround and even a strange and exotic-looking door. You can't see anything out of the window "
                       "though.",
        "items": [
            {"name": "Rune Stone", "type": "quest", "description": "Glows faintly. It's cold and heavy."
                                                                   "\nDon't drop it our it'll make a mess."},
            {"name": "Ancient Coin", "type": "quest", "description": "You can make out a cat's face on it."
                                                                     "\nThat's silly."},
            {"name": "Crystal Shard", "type": "quest", "description": "Feels warm in your hand. It's even tingling."}
        ],
        "next": "third room"
    },
    "third room": {
        "description": "AHH! A gigantic cat! It's sitting right in the middle of grand hall, blocking your path. "
                       "\nIt's eyes are locked on you... Are you it's prey...? "
                       "\nDo something!",
        "items": [
            {"name": "Mystic Dagger", "type": "weapon", "description": "The weapon gleams with ancient energy..."
                                                                       "Maybe this could defeat the cat?"}
        ],
        "next": None
    }
}

#tracks current room
current_room = "first room"

# --- Functions ---

def prompt():
    print("\tWelcome to my game!\n"
          "Explore the rooms to escape this dungeon.\n"
          "Type help for a list of commands.\n")

    input("Press Enter to continue...")
    print("\n You're in a torch-lit room. There's just some ordinary stuff in front of you, "
          "\nbut maybe you should take a closer look..\n")

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if inventory:
        print("Inventory:")
        for item in inventory:
            print(f"- {item['name']}")
    else:
        print("There's nothing in your inventory.. You can pick up something from here.. or you don't...")

def show_room_items():
    # list all items in current room
    room = rooms[current_room]
    print(f"\nYou are in the {current_room}. {room["description"]}")
    if room["items"]:
        print("You see:")
        for item in room["items"]:
            print(f"- {item['name']}")
    else:
        print("Nothing here.")

def find_item(item_name, item_list):
    return next((item for item in item_list if item["name"].lower() == item_name.lower()), None)

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet, removed from room inv
    global inventory
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full. You can't pick up any more items.")
        return
    item = find_item(item_name, rooms[current_room]["items"])
    if item:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        print(f"You picked up the {item['name']}.")
    else:
        print(f"There is no item called {item_name} here.")


def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    global inventory
    item = find_item(item_name, inventory)
    if item:
        inventory.remove(item)
        rooms[current_room]["items"].append(item)
        print(f"You dropped the {item['name']}.")
    else:
        print(f"You don't have the {item_name} in your inventory.")

def use(item_name):
    # Ex: use the item differently depends on the type
    global current_room
    item = find_item(item_name, inventory)
    if not item:
        print(f"You don't have the {item_name} in your inventory.")
        return

    if item['type'] == "food":
        print(f"You eat the {item['name']}. It was tasty.")
        inventory.remove(item)
    elif item['type'] == "weapon" and current_room == "third room":
        print("You raise the Mystic Dagger to strike the cat...")
        print("But before you do.... the cat speaks!")
        print("\n\"Why did you try to attack me??? I was just sitting here!! People have no manners these days.\"")
        print("The cat vanishes. And with it... a door behind it does too. "
              "\nYou're trapped here now... \n")
        exit()
    elif item['type'] == "quest" and item['name'] == "Treats" and current_room == "third room":
        print("You offer the cat treats. The cat purrs and allows you to pass.")
        print("That was so cute! Well done!")
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
    # try to go to the next room
    global current_room
    if current_room == "first room":
        current_room = "second room"
        print("You proceed to the next room.")
    elif current_room == "second room":
        required = {"Rune Stone", "Ancient Coin", "Crystal Shard"}
        if required.issubset(set(item["name"] for item in inventory)):
            current_room = "third room"
            print("The magical door opens as you hold the three special items")
        else:
            print("You can't go further. You need to find the required items.")

    elif current_room == "third room":
        print("The cat blocks your path. You can't go further if you don't use or offer something to interact.")

# --- Game Loop ---

def game_loop():
    prompt()
    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [to the "
                  "next room], quit")
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
        elif command == "go":
            try_next_room()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    game_loop()
