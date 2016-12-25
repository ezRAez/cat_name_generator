import random, string

def generator():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    num = int(input("How many names would you like to choose from? "))
    length_input = int(input("How long do you want the name? "))
    choices = []
    while length_input > 0:
        letter_input = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
        if letter_input == "l":
            choices.append(letter_input)
            length_input = length_input - 1
        elif letter_input == "v":
            choices.append(letter_input)
            length_input = length_input - 1
        elif letter_input == "c":
            choices.append(letter_input)
            length_input = length_input - 1
        else:
            pass
    while(num > 0):
        cat_name = ""
        for letter in choices:
            if letter == "l":
                cat_name = cat_name + random.choice(string.ascii_lowercase)
            elif letter == "v":
                cat_name = cat_name + random.choice(vowels)
            else:
                cat_name = cat_name + random.choice(consonants)
        print(cat_name)
        num -= 1
    return "^ Choose your favorite ^"



print(generator());
