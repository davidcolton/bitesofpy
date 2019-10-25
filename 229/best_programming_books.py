from dataclasses import dataclass
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.request import urlretrieve
import operator

url = "https://bites-data.s3.us-east-2.amazonaws.com/best-programming-books.html"
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


@dataclass
class Book:
    """Book class should instantiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """

    # Data Classes are cool
    # Rank was an issue as the tests had it positionally in position 4
    #   Would have preferred it last.
    #   Worked around it by passing in 0 when creating the class.
    title: str
    author: str
    year: int
    rank: int
    rating: float

    def __str__(self):
        # There must be a better way of printing variable length float precision
        formatted_rating = (
            f"{self.rating:.2f}"
            if f"{self.rating:.2f}"[-1] != "0"
            else f"{self.rating:.1f}"
        )
        return_str = f"[{self.rank:03}] {self.title} ({self.year})\n"
        return_str += f"      {self.author} {formatted_rating}"
        return return_str


def _get_soup(file):
    return BeautifulSoup(file.read_text(), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    books_displayed = 0
    books = load_data()
    for book in books:
        if year == None or book.year >= year:
            print(book)
            books_displayed += 1
        if books_displayed == limit:
            return None


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    # New empty book list
    book_list = []

    # Load the soup object and then locate the books section
    soup = _get_soup(html_file)
    books = soup.find("div", {"class": "books"})

    # Iterate over each of the books.
    for book in books.find_all("div", {"class": "book accepted normal"}):
        # simple try: except: pass if any of the attributes are missing
        try:
            # Get title, author, year, rating
            # Need to make the author lastname, firstname
            # Also need to strip out books not related to Python
            title = book.find("h2", {"class": "main"}).get_text()
            orig_author = book.find("h3", {"class": "authors"}).find("a").get_text()
            author_parts = orig_author.split()
            author = f"{author_parts[-1]}, {' '.join(author_parts[:-1])}"
            year = int(book.find("span", {"class": "date"}).get_text()[-4:])
            rating = float(book.find("span", {"class": "our-rating"}).get_text())
            if "python" in title.lower():
                book_list.append(Book(title, author, year, 0, rating))
        except:
            pass
    # Sort the book list
    # -k.rating sort in descending rating order
    # @clamytoe decided to confuse me by sorting the title in any case other than
    #   the case of the title as extracted from the html
    sorted_book_list = sorted(
        book_list, key=lambda k: (-k.rating, k.year, k.title.title(), k.author)
    )

    # Add the ranking
    for idx, sorted_book in enumerate(sorted_book_list, 1):
        sorted_book.rank = idx

    return sorted_book_list


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""
