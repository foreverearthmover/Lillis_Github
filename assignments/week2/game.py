import time

player_health = 100
player_name = input("Whats your name, traveller?")

def print_animation(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(0.05)

def display_intro():
    print_animation("It's nice to meet you. "
          "You woke up in the woods. You have no idea where you are and how you got here. "
          "You can hear leaves rustling and water trickling.")
    print("It's pitch black outside but you can see something shimmering in the distance.")
    print_animation("What will you do,", player_name, "?")

def update_player_health(change, message):
    global player_health
    player_health += change
    player_health = max(0, player_health)
    print_animation(message)

def end_game():
    if player_health <= 0:
        print_animation("Game Over.")
    else:
        print("You made it out.")

def scenario1():
    print("1. Investigate the strange shimmer.")
    print("2. Stay where you are, look around.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")


    elif choice == "1":
        update_player_health(-5, "You try to sneak up behind a tree without making too much noise. "
                                 "Ouch! You stepped on a pinecone! -5 health \n After a short moment of pain and "
                                 "agony, you concentrate on what's in front of you. \n Is that some kind of... pond? ") # leads to scenario2a

    else:
        update_player_health(0, "Your eyes slowly adjust to the darkness but your surroundings "
                                  "are still hard to make out. \n You start to concentrate on your senses. There's a "
                                  "low, vibrating sound coming from the distance. Is that a voice? Is it calling "
                                  "for you ", player_name, "? ") # leads to scenario2b

def scenario2a():
    print("1. Walk around the body of water.")
    print("2. See if the water is shallow enough to wade through to the other side.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health(-15, "You walk along the edge of the pond for a long time. You start wondering"
                                  " how big the pond might be. \n You keep walking. \n The pain in your foot keeps "
                                  "getting worse. -15 health \n You become anxious thinking about how long you've "
                                  "already been walking. ") # leads to scenario3a
    else:
        update_player_health(-15, "You roll up your pants and carefully place your right foot into the water. "
                                 "It's cold and you can feel rocks beneath you. Every following step hurts. -15 health"
                                 "\n You can hardly make anything out in front of you but you keep going. "
                                 "\n Soon, you arrive at the other end of the.... wait was this a river all along? "
                                 "Damn, thank god you didn't try to walk around the edge, you probably would have "
                                 "gotten lost after a while. ") # leads to scenario3b

def scenario2b():
    print("1. Stand still and keep listening...")
    print("2. Follow the direction of the sound.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health(-90, "After standing still for a moment you sense a shift in the atmosphere "
                                  "\n Something changed. You're not sure what it is. ") # leads to scenario3c
    else:
        update_player_health(0, "You follow the sound, it keeps getting louder and louder until.."
                                "\n It stops. You start to panic, you have no remaining sense of orientation and "
                                "it's gotten... colder? ") # leads to scenario3c

def scenario3a():
    print("1. Keep walking.")
    print("2. Go another direction.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health(0, "You walk. And walk. What feels like a hundred miles. Everything "
                                "hurts and you're losing hope. But it's getting brighter. Then, suddenly, you "
                                "see something in the distance, a field? You rush towards it. It really is a "
                                "field, you made it out. You see houses in the distance. And..people. Where "
                                "are your people? Do you know anyone? Do you even.. speak their language? Are you"
                                "still.. alone? ") # leads to You made it out ending
    else:
        update_player_health(-100, "You turn around and proceed to walk. After only a few minutes in, you "
                                   "realize that you don't remember where you came from, where the river was "
                                   "or how long it's been that you've been lost. It keeps getting worse. All of it. "
                                   "\n Even as the sky turns bright and the trees turn their usual color, the days "
                                   "feel like a dream. You can't tell where the living begins. The sleep becomes "
                                   "the day and the dream becomes the life. You hear a dark voice, calling out... "
                                   "for you... You run towards it but.. it's all one now. \n You lost your mind. " ) # game over

def scenario3b():
    print("1. Keep going forward.")
    print("2. Rest.")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health(-100, "Your foot has gotten worse but you keep going. After what feels like hours "
                                   "of uninterrupted walking, you can't bear the pain anymore. You decide to lift your"
                                   "foot and look at the damage. It's bad. Maybe you shouldn't have kept going. "
                                   "The rocks in the river slashed up your skin and the long distance over the forest "
                                   "floor additionally roughed it up. There's also a layer of dirt and rotten plant "
                                   "mass. You're kinda freaking out. You realize you can't keep going and lay down on "
                                   "the ground. It's so cold. Your wet clothes cling to your frail body. All resources "
                                   "you had left have been used up. The cold wind cuts your skin. You give up.") # game over
    else:
        update_player_health(0, "You end up passing out from the pain. You didn't even notice you "
                                "fell out of consciousness until you're back. It's bright, you can tell, even "
                                "with your eyes closed. You're scared of returning to the nightmare. But there's "
                                "something else - a muffled tone. It becomes clearer - a voice. You open your eyes, "
                                "there's someone! A man walking his dog. You must look deranged but he sees the "
                                "terror on your face and helps you get into his truck. \"Where are we going, then?\", "
                                "he asks. The questions echoes in your mind. \n You don't remember where you came from- "
                                "like... at all.") # leads to You made it out ending


def scenario3c():
    print("1. Don't move. ")
    print("2. Run. ")
    choice = input("Choose your option: ")
    if choice != "1" or choice != "2":
        print("Invalid choice.")
    elif choice == "1":
        update_player_health(-100, "You feel something sharp tear into your neck. Your skin burns, you feel "
                                   "a large amount of warm liquid running down your body and you lose consciousness. ") # game over
    else:
        update_player_health(-100, "For a second, you're stunned. Then, fueled with adrenaline, you dash, "
                                   "you're not sure where. The ground beneath your feet hurts and you almost lose your "
                                   "balance. In the distance there are lights.. or something... getting brighter. "
                                   "But you can't stop. Somethings out to get you and you're sure of it now."
                                   "Then. Suddenly. You fall. \n You're cold all over, your ankles feel like"
                                   "they've been ripped in half. Are you underwater? \n No time to think- You feel "
                                   "everything around you moving, you try to hold onto something but- ") # game over


scenarios = [scenario1, scenario2a, scenario2b, scenario3a, scenario3b, scenario3c]

def play_game():
    display_intro()
    while scenarios and player_health > 0:
        chosen_scenario(scenarios)
        time.sleep(1)
    end_game()

play_game()