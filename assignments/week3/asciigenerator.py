import random
import time

# Art pattern variations
default_animal = "(=ↀωↀ=)"
default_waves = "°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸"

variations_animal = ["ˁ(⦿ᴥ⦿)ˀ", "ヽ(￣(ｴ)￣)ﾉ", "(=^-ω-^=)", "(•ㅅ•)"]
variations_waves = [",.-~*´¨¯¨`*·~-.¸", "ᶫᵒᵛᵉᵧₒᵤ", ":.:.:.:.:.:", "～～～～～"]

def print_animation(*text_parts):
    text = "".join(str(part) for part in text_parts)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

# Welcome and instructions
print_animation("ヾ(＠⌒ー⌒＠)ノ Hey! \nWelcome to my ASCII art application!")

# Main input loop to validate ascii_selection
while True:
    print_animation("What do you want to print?")
    print("a: Animals")
    print("b: Waves")
    print("q: Quit")
    ascii_selection = input("Enter your choice (a/b/q): ").lower()

    if ascii_selection in ["a", "b"]:
        while True:
            try:
                count = int(input("How many times should the pattern repeat (1 to 5)? "))
                if 1 <= count <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("That's not a number... ⊙﹏⊙ Try again.")

        randomize = input("Randomize the pattern? (Y/N): ").upper()
        while randomize not in ["Y", "N"]:
            randomize = input("Please type 'Y' for Yes or 'N' for No ◕‿↼ ").upper()

        # Choose art set
        if ascii_selection == "a":
            base = default_animal
            variations = variations_animal
            message = "They're so cute :3"
        else:
            base = default_waves
            variations = variations_waves
            message = "Don't worry, they won't flush you away "

        print_animation("\nHere it comes...\n")
        for i in range(count):  # how many lines
            line = ""
            for j in range(count):  # how many patterns per line
                if randomize == "Y":
                    line += random.choice(variations)
                else:
                    line += base
            print(line)
        print_animation(message)
        print_animation("\nThanks for using the program :-)")
        break  # end

    elif ascii_selection == "q":
        print_animation("Goodbye!(^ _ ^)/")
        break

    else:
        print_animation("⚠ Invalid choice! Please type a, b, or q.")
