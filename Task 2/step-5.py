import random

# TODO 1 :- Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from stages import stages
lives = 6
# TODO 3 :- Import the logo from hangman_art.py and print it at the start of game.
from log import logo
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    # TODO 6 :- Update the code below to tell the user's how many lives they have left.
    print("**********************<???>/6 LIVES LEFT ****************")
    guess = input("Guess the letter : ").lower()

    # TODO 4 :- if the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letter:
        print(f"You've already guessed  {guess}")
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

    print("Word to guess : "+ display)

    # TODO 5 :- If the letter is not in the chosen word, print out the letter and let them know it's not in the words
    # e.g You guessed d, that's not in your word. You lose a life.

    if guess not in chosen_word:
        lives -= -1
        print(f"You guessed {guess}, that's not in your word. You lose a life")
        if lives == 0:
            game_over = True

            # TODO 7 :- Update the print statement to give the user correct word
            print(f"***********************It Was {chosen_word} YOU LOSE! *********************")

    if "_" not in display:
        game_over = True
        print("*********************** You Win! ************************")

    # TODO 2 :- Update the code below to use the stage list from the file hangman_art
    # That corresponds to the current number of 'lives' the user  has remaining.
    print(stages[lives])
