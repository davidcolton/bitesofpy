from unittest.mock import patch
import pytest
from guess import GuessGame, InvalidNumber, MAX_NUMBER


# Test incorrectly invoking the game
@pytest.mark.parametrize(
    "error_number_to_guess, error",
    [(-5, "Negative number"), (20, "Number too high"), ("string", "Not a number")],
)
def test_incorrectly_invoked(error_number_to_guess, error):
    with pytest.raises(InvalidNumber) as e:
        GuessGame(error_number_to_guess)
    assert str(e.value) == error


# Test invalid input to the game
# Basically same test / expected results as invalidly invoking game
# Except `_validate()` called directly
@pytest.mark.parametrize(
    "error_guess, error",
    [(-5, "Negative number"), (20, "Number too high"), ("string", "Not a number")],
)
def test_invalid_guesses(error_guess, error):
    g = GuessGame(5)
    with pytest.raises(InvalidNumber) as e:
        g._validate(error_guess)
    assert str(e.value) == error


# Test valid input to the game
@pytest.mark.parametrize("guess, responce", [(0, 0), (5, 5), (10.5, 10), (15, 15)])
def test_validate_guess(guess, responce):
    g = GuessGame(5)
    assert g._validate(guess) == responce


# Test the simplest game possible
def test_game():
    g = GuessGame(5)
    assert g.secret_number == 5
    assert g.max_guesses == 5
    assert g.attempt == 0
    assert MAX_NUMBER == 15


@patch("builtins.input", side_effect=[15, 0, "a", 10, 4, 8])
def test_high_low_too_many_guesses(patched_input, capsys):
    g = GuessGame(5)
    g()
    actual = capsys.readouterr()[0].strip()
    expected = "\n".join(
        [
            "Guess a number: ",
            "Too high",
            "Guess a number: ",
            "Too low",
            "Guess a number: ",
            "Enter a number, try again",
            "Guess a number: ",
            "Too high",
            "Guess a number: ",
            "Too low",
            "Guess a number: ",
            "Too high",
            "Sorry, the number was 5",
        ]
    )
    assert actual == expected


@patch("builtins.input", side_effect=[5])
def test_guess_correct(patched_input, capsys):
    g = GuessGame(5)
    g()
    actual = capsys.readouterr()[0].strip()
    expected = "\n".join(["Guess a number: ", "You guessed it!"])
    assert actual == expected
    assert g.attempt == 1

