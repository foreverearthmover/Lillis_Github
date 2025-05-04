# Escape Game - Refactored Version
# In this game, you try to escape from a forest by choosing different actions.
# Each decision will lead to different situations and determine if and how you make it out.
# This is the refactored version, meaning I have made slight adjustments to the code to make it more maintainable

import time # imports module needed for delayed print animation

# constants
ANIMATION_DELAY = 0.03 # seconds between characters
INITIAL_HEALTH = 100 # players health starts at 100
DEBUG = False

PLAYER_NAME = input("What's your name, traveller? ")
player_health = INITIAL_HEALTH # using the constant instead of hardcoded 100

def print_animation(*text_parts): # tuple allows multiple values to be automatically passed
    text = "".join(str(part) for part in text_parts) # all text parts joined into string
    for char in text: # loop through each character of combined string
        print(char, end="", flush=True) # one character at a time, printed on one line
        time.sleep(ANIMATION_DELAY)  # Using the constant instead of hardcoded 0.03
    print()

# Introduction and input player name
def display_intro():
    print_animation("It's nice to meet you, ", PLAYER_NAME, "."
                              "\nYou woke up in the woods. You have no idea where you are "
                              "and how you got here. \nYou can hear leaves rustling and water trickling. ")
    time.sleep(1)
    print("It's pitch black outside but you can see something shimmering in the distance.")
    time.sleep(1)
    print_animation("What will you do, ", PLAYER_NAME, "?")


def update_player_health(change, message):
    global player_health # global variable so that it updates after each scenario, tracking health across the game
    player_health += change # adds/subtracts the change value to current health
    player_health = max(0, player_health) # prevents negative health values
    print_animation(message) # also displays a string
    print("\nYour health is now: ", player_health, "\n")
    if player_health <= 0:
        end_game()
        exit() # player "dies" after choosing options that decrease their player health to 0
    return player_health

def end_game(): # player either "wins" or loses the game; is called after all scenarios of a branch
    if player_health <= 0:
        print_animation("Game Over.")
    else:
        print_animation("You made it out.")

# user chooses one of the actions, choice determines which scenario plays out next
def scenario1():
    print("1. Investigate the strange shimmer.")
    print("2. Stay where you are, look around.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-5, "You try to sneak up behind a tree without making too much noise. "
                                 "Ouch! You stepped on a pinecone! -5 health \nAfter a short moment of pain and "
                                 "agony, you concentrate on what's in front of you. \nIs that some kind of... pond? ")
        scenario2a() # leads to the next scenario
    elif choice == "2":
        update_player_health(0, "Your eyes slowly adjust to the darkness but your surroundings "
                                "are still hard to make out. \nYou start to concentrate on your senses. There's a "
                                "low, vibrating sound coming from the distance. \nIs that a voice? Is it calling "
                                "for you, " + PLAYER_NAME + "? ")
        time.sleep(2)
        scenario2b() # leads to the next scenario
    else:
        print("Invalid choice.")
        scenario1() # resets scenario: takes the user back to the beginning until they enter valid input


def scenario2a():
    print("1. Walk around the body of water.")
    print("2. See if the water is shallow enough to wade through to the other side.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-15, "You walk along the edge of the pond for a long time. You start wondering"
                                  " how big the pond might be. \nYou keep walking. \nThe pain in your foot keeps "
                                  "getting worse. -15 health \nYou become anxious thinking about how long you've "
                                  "already been walking. ")
        time.sleep(2)
        scenario3a() # leads to the next scenario
    elif choice == "2":
        update_player_health(-15, "You roll up your pants and carefully place your right foot into the water. "
                                  "It's cold and you can feel rocks beneath you. Every following step hurts. -15 health"
                                  "\nYou can hardly make anything out in front of you but you keep going. "
                                  "\nSoon, you arrive at the other end of the.... wait was this a river all along? "
                                  "\nDamn, thank god you didn't try to walk around the edge, you probably would have "
                                  "gotten lost after a while. ")
        time.sleep(2)
        scenario3b() # leads to the next scenario
    else:
        print("Invalid choice.")
        scenario2a() # resets scenario


def scenario2b():
    print("1. Stand still and keep listening...")
    print("2. Follow the direction of the sound.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-10, "After standing still for a moment you sense a shift in the atmosphere "
                                  "\nSomething changed. You're not sure what it is. ")
        time.sleep(2)
        scenario3c() # leads to the next scenario
    elif choice == "2":
        update_player_health(0, "You follow the sound, it keeps getting louder and louder until.."
                                "\nIt stops. You start to panic, you have no remaining sense of orientation and "
                                "\nit's gotten... colder? ")
        time.sleep(2)
        scenario3c() # leads to the next scenario
    else:
        print("Invalid choice.")
        scenario2b() # resets scenario


def scenario3a():
    print("1. Keep walking.")
    print("2. Go another direction.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(0, "You walk. And walk. What feels like a hundred miles. Everything "
                                "hurts and you're losing hope. But it's getting brighter.\nThen, suddenly, you "
                                "see something in the distance, a field? \nYou rush towards it. It really is a "
                                "field, you made it out. You see houses in the distance. And..people. \nWhere "
                                "are your people? Do you know anyone? Do you even.. speak their language? Are you "
                                "still.. alone? ")
        time.sleep(2)
        end_game() # ending a1: all scenarios of the branch have been played
    elif choice == "2":
        update_player_health(-100, "You turn around and proceed to walk. After only a few minutes in, \nyou "
                                   "realize that you don't remember where you came from, where the river was "
                                   "or how long it's been that you've been lost. \nIt keeps getting worse. All of it. "
                                   "\nEven as the sky turns bright and the trees turn their usual color, the days "
                                   "feel like a dream. You can't tell where the living begins. \nThe sleep becomes "
                                   "the day and the dream becomes the life. You hear a dark voice, calling out... "
                                   "for you... You run towards it but.. 𝐢⃥⃒̸𝐭⃥⃒̸'⃥⃒̸𝐬⃥⃒̸ 𝐚⃥⃒̸𝐥⃥⃒̸𝐥⃥⃒̸ 𝐨⃥⃒̸𝐧⃥⃒̸𝐞⃥⃒̸ 𝐧⃥⃒̸𝐨⃥⃒̸𝐰⃥⃒̸. \nYou lost your mind. ")
        time.sleep(2)
        end_game() # ending a2
    else:
        print("Invalid choice.")
        scenario3a() # resets scenario


def scenario3b():
    print("1. Keep going forward.")
    print("2. Rest.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-100, "Your foot has gotten worse but you keep going. \nAfter what feels like hours "
                                   "of uninterrupted walking, you can't bear the pain anymore. You decide to lift up your "
                                   "foot and look at the damage. \nIt's bad. Maybe you shouldn't have kept going. "
                                   "\nThe rocks in the river slashed up your skin and the long distance over the forest "
                                   "floor additionally roughed it up. \nThere's also a layer of dirt and rotten plant "
                                   "mass. You're kinda freaking out. \nYou realize you can't keep going and lay down on "
                                   "the ground. \nIt's so cold. \nYour wet clothes cling to your frail body. All resources "
                                   "you had left have been used up. The cold wind cuts your skin."
                                   "\n You give up. ")
        time.sleep(2)
        end_game() # ending b1
    elif choice == "2":
        update_player_health(0, "You end up passing out from the pain. \nYou didn't even notice you "
                                "fell out of consciousness until you're back. \nIt's bright, you can tell, even "
                                "with your eyes closed. \nYou're scared of returning to the nightmare. But there's "
                                "something else - \na muffled tone. It becomes clearer - a voice. \nYou open your eyes, "
                                "there's someone! A man walking his dog. \nYou must look deranged but he sees the "
                                "terror on your face and helps you get into his truck. \"Where are we going, then?\", "
                                "he asks. The question echoes in your mind. \nYou don't remember where you came from- "
                                "like... at all.")
        time.sleep(2)
        end_game() # ending b2
    else:
        print("Invalid choice.")
        scenario3b() # resets scenario


def scenario3c():
    print("1. Don't move.")
    print("2. Run.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-100, "You feel something sharp tear into your neck. Your skin burns, you feel "
                                   "a large amount of warm liquid running down your body.")
        time.sleep(2)
        print_animation("You lose consciousness.")
        time.sleep(1)
        end_game() # ending c1
    elif choice == "2":
        update_player_health(-100, "For a second, you're stunned. Then, fueled with adrenaline, you dash, "
                                   "you're not sure where. \nThe ground beneath your feet hurts and you almost lose your "
                                   "balance. \nIn the distance there are lights.. or something... getting brighter. "
                                   "But you can't stop. \nSomethings out to get you and you're sure of it now. "
                                   "Then. Suddenly. You fall. \nYou're cold all over, your ankles feel like "
                                   "they've been ripped in half. Are you underwater? \nNo time to think- You feel "
                                   "everything around you moving, you try to hold onto something but- ")
        time.sleep(2)
        end_game() # ending c2
    else:
        print("Invalid choice.")
        scenario3c() # resets scenario


def main():
    display_intro() # first user input and introduction to the game's objective
    scenario1() # start of game: first branch


if __name__ == "__main__":
    main() # entry point of the game