import random
world_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(world_list)
print(chosen_word)

# TODO 1 :- Create a placeholder with the same number of blanks of the chosen_word

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess the letter : ")

# Create a display that's puts guss letter in the right position and _ at the rest of the string.

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)


