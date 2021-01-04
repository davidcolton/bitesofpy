from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int, day_of_year: int = None) -> bool:
    if not day_of_year:
        day_of_year = datetime.now().timetuple().tm_yday
    return (
        False if books_read == 0 else (books_read / books_goal) >= (day_of_year / 365)
    )
