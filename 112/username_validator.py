# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple("Validator", "range regex")


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    platform_dict = dict()

    for platform in social_platforms.split("\n\n"):
        lines = list(filter(None, platform.split("\n")))
        platform = lines[0].strip()
        temp_dict = dict()
        for line in lines[1:]:
            key, value = line.split(":")
            temp_dict[key.strip()] = value.strip()

        p_range = range(int(temp_dict["Min"]), int(temp_dict["Max"]))
        temp_dict["Can contain"] = re.sub(" ", "", temp_dict["Can contain"])
        p_regex = re.compile(r"[" + temp_dict["Can contain"] + "]")

        platform_dict[platform] = Validator(p_range, p_regex)

    return platform_dict


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators.keys():
        raise ValueError

    validator = all_validators[platform]

    reg = validator.regex
    ran = validator.range

    if len(username) in ran and all(
        [reg.search(username[c]) for c in range(0, len(username))]
    ):
        return True
    else:
        return False
