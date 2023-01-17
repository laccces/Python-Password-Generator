import random

word_list = []
password = []

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
    first_word = word_picker()
    password.append(first_word.capitalize())
    password.append(str(random.randrange(100, 1000)))
    second_word = word_picker()
    password.append(second_word)
    print("".join(password))

i = 0

while i < 5:
    password_generator()
    password = []
    i += 1

