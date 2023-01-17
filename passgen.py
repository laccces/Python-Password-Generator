import random

word_list = []

def generate_words():
    f = open("words.txt", "r")
    for word in f:
        if len(word) > 5 and len(word) < 12:
            word_list.append(word.strip())

generate_words()

def word_picker():
    num = random.randrange(0, 5)
    return word_list[num]

def password_generator():
    print(f"{word_picker().capitalize()}{random.randrange(100,1000)}{word_picker()}")

i = 0

while i < 5:
    password_generator()
    i += 1
