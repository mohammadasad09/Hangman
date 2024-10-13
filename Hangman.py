import random
import string
from ascii_art import stages

def load_words(filename):
    with open(filename) as file_in:
        return [line.strip() for line in file_in]

def display_current_state(display_word):
    print(" ".join(display_word))

def get_valid_letter_input(guessed_letters):
    while True:
        guessed_letter = input("Guess a letter: ").lower()
        if guessed_letter not in string.ascii_letters:
            print("Invalid input. Please enter a letter.")
        elif guessed_letter in guessed_letters:
            print(f"You've already guessed '{guessed_letter}'. Try again.")
        else:
            return guessed_letter

def play_game(word_list):
    random_word = random.choice(word_list)
    display_word = ["_" for _ in random_word]
    allowed_attempts = 7
    guessed_letters = []
    
    print("Welcome to Hangman!")

    
    while allowed_attempts > 0:
        
        display_current_state(display_word)
        guessed_letter = get_valid_letter_input(guessed_letters)
        guessed_letters.append(guessed_letter)

        if guessed_letter in random_word:
            for i, letter in enumerate(random_word):
                if letter == guessed_letter:
                    display_word[i] = guessed_letter
            print("Correct guess!")
        else:
            allowed_attempts -= 1
            print(stages[allowed_attempts])
            print(f"Incorrect guess. You have {allowed_attempts} attempts left.")
        
        if "_" not in display_word:
            print(f"Congratulations, you won! The word was '{random_word}'.")
            return

    print(f"Sorry, you lost. The word was '{random_word}'.")

def main():
    word_list = load_words("words.txt")
    resume_game = "yes"

    while resume_game == "yes":
        play_game(word_list)
        resume_game = input("Would you like to play again? (yes or no): ").lower()
        while resume_game not in ["yes", "no"]:
            resume_game = input("Invalid input. Please enter 'yes' or 'no': ").lower()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
