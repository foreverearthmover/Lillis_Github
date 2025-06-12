import cowsay
import pyjokes
import helper
import random

joke = pyjokes.get_joke()
rambling = helper.text_model.make_short_sentence(280)
choice_list = [joke,rambling]

cowsay.kitty(random.choice(choice_list))

# cowsay character either displays a joke from pyjokes or random text
# generated with markovify from helper.py