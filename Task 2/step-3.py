import random
from Tools.scripts.dutree import display

world_list = ["aardvark","baboon","camel"]

chosen_word = random.choice(world_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO 1 :- use a while loop to let the user guess again.

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess the letter : ").lower()

    display = ""


    # TODO 2 :- change the for loop so that you keep the previous correct letter in display string.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)
