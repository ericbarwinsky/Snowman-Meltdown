import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = []
    for char in secret_word:
        if char in guessed_letters:
            display_word.append(char)
        else:
            display_word.append("_")
    print(f"Secret word selected: " + " ".join(display_word))


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

    while mistakes != 3:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
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

    if mistakes == 3:
        print(f"Game Over! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()