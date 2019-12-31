from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (
    get_signs,
    get_sign_with_most_famous_people,
    signs_are_mutually_compatible,
    get_sign_by_date,
)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope="module")
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_verify_signs_type(signs):
    assert type(signs[0]).__name__ == "Sign"


@pytest.mark.parametrize(
    "arg, expected",
    [
        (datetime(2016, 2, 29), "Pisces"),
        (datetime(2018, 3, 20), "Pisces"),
        (datetime(2018, 3, 21), "Aries"),
        (datetime(2018, 4, 11), "Aries"),
        (datetime(2018, 4, 19), "Aries"),
        (datetime(2018, 4, 20), "Taurus"),
    ],
)
def test_get_sign_by_date(signs, arg, expected):
    assert get_sign_by_date(signs, arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (datetime(2016, 2, 29), "Taurus"),
        (datetime(2018, 3, 20), "Taurus"),
        (datetime(2018, 3, 21), "Pisces"),
        (datetime(2018, 4, 11), "Pisces"),
        (datetime(2018, 4, 19), "Pisces"),
        (datetime(2018, 4, 20), "Aries"),
    ],
)
def test_get_sign_by_date_negative_tests(signs, arg, expected):
    assert not get_sign_by_date(signs, arg) == expected


@pytest.mark.parametrize(
    "sign_01, sign_02",
    [
        ("Gemini", "Taurus"),
        ("Taurus", "Sagittarius"),
        ("Taurus", " Aquarius"),
        ("Sagittarius", "Taurus"),
    ],
)
def test_signs_are_mutually_compatible(signs, sign_01, sign_02):
    assert not signs_are_mutually_compatible(signs, sign_01, sign_02)


@pytest.mark.parametrize(
    "sign_01, sign_02",
    [
        ("Gemini", "Aries"),
        ("Aries", "Gemini"),
        ("Gemini", " Aquarius"),
        ("Aquarius", " Gemini"),
    ],
)
def test_signs_are_not_mutually_compatible(signs, sign_01, sign_02):
    assert signs_are_mutually_compatible(signs, sign_01, sign_02)


def test_get_sign_with_most_famous_people(signs):
    s = get_sign_with_most_famous_people(signs)
    assert s[0] == "Scorpio"
    assert s[1] == 35
