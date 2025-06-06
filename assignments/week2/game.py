import time

player_health = 100
player_name = input("What's your name, traveller? ")

def print_animation(*text_parts):
    text = "".join(str(part) for part in text_parts)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

def display_intro():
    print_animation("It's nice to meet you, ", player_name, ". "
          "You woke up in the woods. You have no idea where you are and how you got here. "
          "\nYou can hear leaves rustling and water trickling. ")
    time.sleep(1)
    print("It's pitch black outside but you can see something shimmering in the distance.")
    time.sleep(1)
    print_animation("What will you do, ", player_name, "?")

def update_player_health(change, message):
    global player_health
    player_health += change
    player_health = max(0, player_health)
    print_animation(message)
    print("\nYour health is now:", player_health, "\n")
    if player_health <= 0:
        end_game()
        exit()

def end_game():
    if player_health <= 0:
        print_animation("Game Over.")
    else:
        print_animation("You made it out.")

def scenario1():
    print("1. Investigate the strange shimmer.")
    print("2. Stay where you are, look around.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-5, "You try to sneak up behind a tree without making too much noise. "
                                 "Ouch! You stepped on a pinecone! -5 health \nAfter a short moment of pain and "
                                 "agony, you concentrate on what's in front of you. \nIs that some kind of... pond? ")
        scenario2a()
    elif choice == "2":
        update_player_health(0, "Your eyes slowly adjust to the darkness but your surroundings "
                                  "are still hard to make out. \nYou start to concentrate on your senses. There's a "
                                  "low, vibrating sound coming from the distance. \nIs that a voice? Is it calling "
                                  "for you, " + player_name + "? ")
        time.sleep(2)
        scenario2b()
    else:
        print("Invalid choice.")
        scenario1()

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
        scenario3a()
    elif choice == "2":
        update_player_health(-15, "You roll up your pants and carefully place your right foot into the water. "
                                  "It's cold and you can feel rocks beneath you. Every following step hurts. -15 health"
                                  "\nYou can hardly make anything out in front of you but you keep going. "
                                  "\nSoon, you arrive at the other end of the.... wait was this a river all along? "
                                  "\nDamn, thank god you didn't try to walk around the edge, you probably would have "
                                  "gotten lost after a while. ")
        time.sleep(2)
        scenario3b()
    else:
        print("Invalid choice.")
        scenario2a()

def scenario2b():
    print("1. Stand still and keep listening...")
    print("2. Follow the direction of the sound.")
    choice = input("Choose your option: ")
    if choice == "1":
        update_player_health(-10, "After standing still for a moment you sense a shift in the atmosphere "
                                  "\nSomething changed. You're not sure what it is. ")
        time.sleep(2)
        scenario3c()
    elif choice == "2":
        update_player_health(0, "You follow the sound, it keeps getting louder and louder until.."
                                "\nIt stops. You start to panic, you have no remaining sense of orientation and "
                                "\nit's gotten... colder? ")
        time.sleep(2)
        scenario3c()
    else:
        print("Invalid choice.")
        scenario2b()

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
        end_game()
    elif choice == "2":
        update_player_health(-100, "You turn around and proceed to walk. After only a few minutes in, \nyou "
                                   "realize that you don't remember where you came from, where the river was "
                                   "or how long it's been that you've been lost. \nIt keeps getting worse. All of it. "
                                   "\nEven as the sky turns bright and the trees turn their usual color, the days "
                                   "feel like a dream. You can't tell where the living begins. \nThe sleep becomes "
                                   "the day and the dream becomes the life. You hear a dark voice, calling out... "
                                   "for you... You run towards it but.. 𝐢⃥⃒̸𝐭⃥⃒̸'⃥⃒̸𝐬⃥⃒̸ 𝐚⃥⃒̸𝐥⃥⃒̸𝐥⃥⃒̸ 𝐨⃥⃒̸𝐧⃥⃒̸𝐞⃥⃒̸ 𝐧⃥⃒̸𝐨⃥⃒̸𝐰⃥⃒̸. \nYou lost your mind. ")
        time.sleep(2)
        end_game()
    else:
        print("Invalid choice.")
        scenario3a()

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
        end_game()
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
        end_game()
    else:
        print("Invalid choice.")
        scenario3b()

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
        end_game()
    elif choice == "2":
        update_player_health(-100, "For a second, you're stunned. Then, fueled with adrenaline, you dash, "
                                   "you're not sure where. \nThe ground beneath your feet hurts and you almost lose your "
                                   "balance. \nIn the distance there are lights.. or something... getting brighter. "
                                   "But you can't stop. \nSomethings out to get you and you're sure of it now. "
                                   "Then. Suddenly. You fall. \nYou're cold all over, your ankles feel like "
                                   "they've been ripped in half. Are you underwater? \nNo time to think- You feel "
                                   "everything around you moving, you try to hold onto something but- ")
        time.sleep(2)
        end_game()
    else:
        print("Invalid choice.")
        scenario3c()

def play_game():
    display_intro()
    scenario1()

play_game()
