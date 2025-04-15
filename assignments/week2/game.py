import time

player_health = 100
player_name = input("Whats your name, traveller?")

def display_intro():
    print("It's nice to meet you. "
          "You woke up in the woods. You have no idea where you are and how you got here. "
          "You can hear leaves rustling and water trickling.")
    print("It's pitch black outside but you can see something shimmering in the distance.")
    print("What will you do,",player_name, "?")

def update_player_health(change, message):
    global player_health
    player_health += change
    print(message)

def end_game():
    if player_health <= 0:
        print("Game Over.")
    else:
        print("You made it out.")

def scenario1():
    print("1. Investigate the strange shimmer")
    print("2. Stay where you are, look around.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")


    elif choice == "1":
        update_player_health(95, "You try to sneak up behind a tree without making too much noise. "
                                 "Ouch! You stepped on a pinecone! -5 health \n After a short moment of pain and "
                                 "agony, you concentrate on what's in front of you. \n Is that some kind of... pond?") # scenario2a

    else:
        update_player_health(100, "Your eyes slowly adjust to the darkness but your surroundings "
                                  "are still hard to make out. \n You start to concentrate on your senses. There's a "
                                  "low, vibrating sound coming from the distance. ") # scenario2b

def scenario2a():
    print("1. Walk around the body of water.")
    print("2. See if the water is shallow enough to wade through to the other side.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health()
    else:
        update_player_health()

def scenario2b():
    print("1. Stand still and keep listening...")
    print("2. Follow the direction of the sound.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health()
    else:
        update_player_health()

def scenario3a():
    print("1. ")
    print("2. ")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health()
    else:
        update_player_health()

def scenario3b():
    print("1. ")
    print("2. ")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health()
    else:
        update_player_health()


def scenario3c():
    print("1. ")
    print("2. ")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health()
    else:
        update_player_health()


def scenario3d():
    print("1. ")
    print("2. ")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health()
    else:
        update_player_health()


scenarios = [scenario1, scenario2a, scenario2b, scenario3a, scenario3b, scenario3c, scenario3d]

def play_game():
    display_intro()
    while scenarios and player_health > 0:
        chosen_scenario(scenarios)
        time.sleep(1)
    end_game()

play_game()