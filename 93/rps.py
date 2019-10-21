from random import choice

defeated_by = dict(paper="scissors", rock="paper", scissors="rock")
lose = "{} beats {}, you lose!"
win = "{} beats {}, you win!"
tie = "tie!"


def _get_computer_move():
    """Randomly select a move"""
    return choice(list(defeated_by.keys()))


def _get_winner(computer_choice, player_choice):
    """Return above lose/win/tie strings populated with the
       appropriate values (computer vs player)"""
    if player_choice == "q":
        raise RuntimeError
    elif player_choice not in defeated_by.keys():
        result = "Invalid choice, please go again"
    elif computer_choice == player_choice:
        result = tie
    elif defeated_by[computer_choice] == player_choice:
        result = win.format(player_choice, computer_choice)
    else:
        result = lose.format(computer_choice, player_choice)
    return result


def game():
    """Game loop, receive player's choice via the generator's
       send method and get a random move from computer (_get_computer_move).
       Raise a StopIteration exception if user value received = 'q'.
       Check who wins with _get_winner and print its return output."""
    result = "Welcome to Rock Paper Scissors"
    while True:
        player_choice = yield result
        result = _get_winner(_get_computer_move(), player_choice)
        print(result)
