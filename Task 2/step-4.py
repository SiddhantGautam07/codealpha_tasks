import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

world_list = ["aardvark","baboon","camel"]

# TODO 1 :- Create a variable called 'lives' to keep track of the how many lives of user has left.
# set 'lives' is equal to 6.
lives = 6

chosen_word = random.choice(world_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

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

    # TODO 2 :- If guess is not listed in the chosen_word, Then reduce 'lives' by 1.
    # If lives goes to 0 then the game should stop and it should print "You Loose".

    if guess not in chosen_word:
        lives -= -1
        if lives == 0:
            game_over = True
            print("You Lose!")

    if "_" not in display:
        game_over = True
        print("You Win!")

    # TODO 3 :- print the ASCII art from stages.
    # That corresponds to the current number of 'lives' the user  has remaining.
    print(stages[lives])
