from collections import namedtuple
from datetime import date, datetime
from dateutil.parser import parse
from time import mktime

import feedparser

FEED = "http://projects.bobbelderbos.com/pcc/all.rss.xml"

Entry = namedtuple("Entry", "date title link tags")


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return datetime.fromtimestamp(mktime(stime)).date()


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    feed_entries = []
    feed = feedparser.parse(FEED)
    for post in feed["entries"]:
        # Sort out the date
        post_date = _convert_struct_time_to_dt(post.published_parsed)
        post_title = post.title
        post_link = post.link
        post_tags = []
        for tag in post.tags:
            post_tags.append(tag.term.lower())
        feed_entries.append(Entry(post_date, post_title, post_link, post_tags))

    return feed_entries


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    search = search.lower()
    if "&" in search:
        search_terms = search.split("&")
        return (
            True if all(term.strip() in entry.tags for term in search_terms) else False
        )
    elif "|" in search:
        search_terms = search.split("|")
        return (
            True if any(term.strip() in entry.tags for term in search_terms) else False
        )
    elif search in entry.tags:
        return True
    else:
        return False


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date desc
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()

    # Get the max title length for clean printing
    title_length = max([len(ent.title) for ent in entries])

    while True:
        search = input("Search for (q for exit): ")
        if search == "":
            print("Please provide a search term")
            continue
        elif search == "q":
            print("Bye")
            break
        found_entries = []
        for entry in entries:
            if filter_entries_by_tag(search, entry):
                found_entries.append(entry)

        # Number of entries found
        num_entries = len(found_entries)

        # Print out each found entry
        for entry in sorted(found_entries, key=lambda x: x.date):
            print(
                f"{entry.date:%Y-%m-%d} | {entry.title:<{title_length}} | {entry.link}"
            )
        print()

        word = "entry" if num_entries == 1 else "entries"

        print(f'{num_entries} {word} matched "{search}"')


if __name__ == "__main__":
    main()
