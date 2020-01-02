import os

import pytest

from movies import MovieDb

DB = os.path.join(os.getenv("TMP", "/tmp"), "movies.db")
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = "movies"


@pytest.fixture
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)

    # If the movie database exists better to just remove it and create clean
    if os.path.exists(DB):
        os.remove(DB)

    # Create the movies database
    m_db = MovieDb(DB, DATA, TABLE)
    m_db.init()

    yield m_db

    m_db.drop_table()


# write tests for all MovieDb's query / add / delete
def test_query_blank(db):
    results = db.query()

    # Verify all rows returned
    assert len(results) == 10

    # Verify the first result
    assert results[0][0] == 1
    assert results[0][1] == "The Godfather"
    assert results[0][2] == 1972
    assert results[0][3] == 9.2

    # Verify the last result
    assert results[9][0] == 10
    assert results[9][1] == "Lawrence of Arabia"
    assert results[9][2] == 1962
    assert results[9][3] == 8.3


def test_query_single_title(db):
    results = db.query(title="Cuckoo")

    # Verify rows returned
    assert len(results) == 1

    # Verify the first result
    assert results[0][0] == 9
    assert results[0][1] == "One Flew Over the Cuckoo's Nest"
    assert results[0][2] == 1975
    assert results[0][3] == 8.7


def test_query_multiple_titles(db):
    results = db.query(title="of")

    # Verify rows returned
    assert len(results) == 2

    # Verify the first result
    assert results[0][1] == "The Wizard of Oz"
    assert results[1][1] == "Lawrence of Arabia"


def test_query_single_year(db):
    results = db.query(year=1980)

    # Verify rows returned
    assert len(results) == 1

    # Verify the first result
    assert results[0][0] == 4
    assert results[0][1] == "Raging Bull"
    assert results[0][2] == 1980
    assert results[0][3] == 8.2


def test_query_multiple_years(db):
    results = db.query(year=1939)

    # Verify rows returned
    assert len(results) == 2

    # Verify the first result
    assert results[0][1] == "Gone with the Wind"
    assert results[1][1] == "The Wizard of Oz"


def test_query_single_score(db):
    results = db.query(score_gt=9.2)

    # Verify rows returned
    assert len(results) == 1

    # Verify the first result
    assert results[0][0] == 2
    assert results[0][1] == "The Shawshank Redemption"
    assert results[0][2] == 1994
    assert results[0][3] == 9.3


def test_query_multiple_scores(db):
    results = db.query(score_gt=9.1)

    # Verify rows returned
    assert len(results) == 2

    # Verify the first result
    assert results[0][1] == "The Godfather"
    assert results[1][1] == "The Shawshank Redemption"


def test_query_no_results(db):
    results = db.query(title="Toy Story")
    assert len(results) == 0
    results = db.query(year=202)
    assert len(results) == 0
    results = db.query(score_gt=9.9)
    assert len(results) == 0


def test_multiple_query_parameters(db):
    # Only first query parameter should be used
    results = db.query(title="Cuckoo", year=1980)

    # Verify rows returned
    assert len(results) == 1
    assert results[0][1] == "One Flew Over the Cuckoo's Nest"

    # Only first query parameter should be used
    results = db.query(year=1980, score_gt=9.1)

    # Verify rows returned
    assert len(results) == 1
    assert results[0][1] == "Raging Bull"


def test_add_and_delete_rows(db):
    assert db.add("Toy Story", 1995, 8.3) == 11
    assert db.add("Toy Story 2", 1999, 7.9) == 12

    # Search and verify that they're there
    results = db.query(title="Toy Story")
    assert len(results) == 2

    # Delete Toy Story
    db.delete(11)

    # Search and verify Toy Story 2 is still there
    results = db.query(title="Toy Story")
    assert len(results) == 1
    assert results[0][1] == "Toy Story 2"

