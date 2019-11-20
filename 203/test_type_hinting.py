from typing import get_type_hints
import pytest

from type_hinting import Employee


@pytest.fixture(scope="module")
def mohh():
    return Employee("Mohhinder", "Suresh", 5, 8, 12.75)


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("first_name", str),
        ("last_name", str),
        ("days_per_week", int),
        ("hours_per_day", float),
        ("wage", float),
    ],
)
def test_employee(mohh, arg, expected):
    anno = get_type_hints(mohh)
    assert anno[arg] == expected


@pytest.mark.parametrize(
    "arg, expected", [("number", float), ("places", int), ("return", str)]
)
def test_rounder(mohh, arg, expected):
    anno = get_type_hints(mohh._rounder)
    assert anno[arg] == expected


def test_weekly_pay(mohh):
    assert get_type_hints(Employee.weekly_pay.fget)["return"] == str

