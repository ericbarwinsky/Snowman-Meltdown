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


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []
    while mistakes != 3:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess not in secret_word:
            mistakes += 1
        else:
            guessed_letters.append(guess)

if __name__ == "__main__":
    play_game()