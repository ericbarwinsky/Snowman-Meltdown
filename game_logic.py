import random

import ascii_art as aa


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_validated_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1:
            if guess.isalpha():
                return guess.lower()


def display_game_state(mistakes, secret_word, guessed_letters):
    print(aa.STAGES[mistakes])
    display_word = []
    for char in secret_word:
        if char in guessed_letters:
            display_word.append(char)
        else:
            display_word.append("_")
    print(f"Secret word selected: " + " ".join(display_word))


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def right_word(secret_word, guessed_letters):
    letters_secret_word = set(secret_word)
    set_guessed_letters = set(guessed_letters)
    all_guessed = letters_secret_word.issubset(set_guessed_letters)
    return all_guessed


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []
    letter_game_list =[]

    while mistakes != 5:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_validated_input()
        print("You guessed:", guess)

        if guess in letter_game_list:
            print("You already guessed that letter.")
        elif guess not in secret_word:
            letter_game_list.append(guess)
            mistakes += 1
        else:
            guessed_letters.append(guess)
            letter_game_list.append(guess)

        if right_word(secret_word, guessed_letters):
            print("Congratulation! you have safed the snowman!")
            break

    if mistakes == 5:
        print(aa.STAGES[mistakes])
        print(f"Game Over! The word was: {secret_word}")
