import game_logic as gl


def get_info_next_round():
    """
        Asks the user if they want to play another round.
        Returns True for 'y' (Yes) and False for 'n' (No).
    """

    while True:
        next_round = input("\nDo you want another round? Yes(Y) No(N) ")
        next_round = next_round.lower()
        match next_round:
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Please enter 'y' for yes or 'n' for no.")
                continue


def main():
    """
        The entry point of the program. Manages the high-level flow by
        starting new games and handling the program exit.
    """

    while True:
        gl.play_game()
        if not get_info_next_round():
            print("Bye")
            break


if __name__ == "__main__":
    main()