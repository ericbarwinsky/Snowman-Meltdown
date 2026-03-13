import game_logic as gl


def get_info_next_round():
    while True:
        next_round = input("\nDo you want another round? Yes(Y) No(No) ")
        next_round = next_round.lower()
        match next_round:
            case "y":
                return True
            case "n":
                return False
            case _:
                continue


def main():
    while True:
        gl.play_game()
        if not get_info_next_round():
            break





if __name__ == "__main__":
    main()