import random
import string
from ascii_art import stages


from animals import animals 
from geography import geography
from movies import movies

def game_settings(selected_subject, selected_difficulty):

    difficulty_levels = ["easy", "medium", "difficult", "professional", "impossible"]
    if selected_subject == "movies":
        return movies[difficulty_levels.index(selected_difficulty)]
    elif selected_subject == "animals":
        return animals[difficulty_levels.index(selected_difficulty)]
    else:
        return geography[difficulty_levels.index(selected_difficulty)]

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
    random_word = random.choice(word_list).lower()
    display_word = ["_" if letter != " " else " " for letter in random_word]
    allowed_attempts = 7
    guessed_letters = []
    
    print("Welcome to Hangman!")
    
    while allowed_attempts > 0:

        print("\nCurrent word: " + " ".join(display_word))
        guessed_letter = get_valid_letter_input(guessed_letters)
        guessed_letters.append(guessed_letter)

        if guessed_letter in random_word:
            # Update all occurrences of guessed_letter in display_word
            for i, letter in enumerate(random_word):
                if letter == guessed_letter:
                    display_word[i] = guessed_letter
            print(f"Correct guess! The letter '{guessed_letter}' is in the word.")
        else:
            allowed_attempts -= 1
            print(stages[allowed_attempts])
            print(f"Incorrect guess. You have {allowed_attempts} attempts left.")
        
        # Check if the word has been fully guessed
        if "_" not in display_word:
            print(f"Congratulations, you won! The word was '{random_word}'.")
            return

    print(f"Sorry, you lost. The word was '{random_word}'.")


def main():

    list_of_words = []

    category_chosen = input("What category would you like to choose: \n 1. Movies \n 2. Geography \n 3. Animals \n" ).lower()
    difficulty_chosen = input("What is the difficult you would like to choose: \n 1. Easy \n 2. Medium \n 3. Difficult \n 4. Professional \n 5. Impossible \n").lower()
    
    list_of_words = game_settings(selected_subject = category_chosen, selected_difficulty = difficulty_chosen)

    resume_game = "yes"
    while resume_game == "yes":
        play_game(list_of_words)
        resume_game = input("Would you like to play again? (yes or no): ").lower()
        while resume_game not in ["yes", "no"]:
            resume_game = input("Invalid input. Please enter 'yes' or 'no': ").lower()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
