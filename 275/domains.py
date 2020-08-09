from collections import Counter
from bs4 import BeautifulSoup
import requests

COMMON_DOMAINS = "https://bites-data.s3.us-east-2.amazonaws.com/common-domains.html"
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    r = requests.get(COMMON_DOMAINS)
    soup = BeautifulSoup(r.text, "html.parser")
    return [
        row.select("td")[2].get_text(strip=True)
        for row in soup.find("div", TARGET_DIV).findChildren("tr")
    ]


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    not_common = Counter(
        [
            email_tup[1]
            for email_tup in (email.split("@") for email in emails)
            if email_tup[1] not in common_domains
        ]
    )

    return list(not_common.most_common())
