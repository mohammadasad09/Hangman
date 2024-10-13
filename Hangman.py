
import random
import string

word_list = ["ardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
blanks = []
allowed_attempts = 7

random_word = str(random.choice(word_list))


print("Welcome to hangman!")
for x in range(len(random_word)):
    blanks.append("_")

while allowed_attempts != 0:
    
    print(*blanks)
    guessed_letter = input("Guess a letter: ").lower()
    #Runs an entire check through the word    
    for x in range(len(random_word)):
        
        if guessed_letter == random_word[x]:
            blanks[x] = guessed_letter
   
    print(*blanks)
    
    if guessed_letter in random_word:
        print("You have guessed correctly.")
    else:
        allowed_attempts -= 1
        print(stages[allowed_attempts])
        print(f"You have guessed incorrectly. You have {allowed_attempts} left.")
    
    if list(random_word) == blanks:
        break


if allowed_attempts == 0:
    print(f"You have lost the game. The correct word was {random_word}.")
else:
    print(f"Congratulations, you won. The correct word was {random_word}.")

