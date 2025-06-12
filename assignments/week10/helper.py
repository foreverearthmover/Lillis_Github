import markovify

with open("corpus.txt") as f:
    text = f.read()

text_model = markovify.Text(text)
