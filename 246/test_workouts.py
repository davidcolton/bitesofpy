import pytest
import sys

from workouts import print_workout_days


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("body", "Mon, Tue, Thu, Fri\n"),
        ("strength", "No matching workout\n"),
        ("cardio", "Wed\n"),
    ],
)
def test_print_workout_days(capsys, arg, expected):
    print_workout_days(arg)
    out, err = capsys.readouterr()
    assert out == expected

