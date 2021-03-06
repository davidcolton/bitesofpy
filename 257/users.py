pw1 = """
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
"""


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    passwd_dict = dict()

    lines = [line.strip() for line in passwd.split("\n") if line != ""]
    for line in lines:
        username, _, _, _, name, *ignore = line.split(":")
        name = (
            "unknown"
            if name.strip() == ""
            else " ".join(name.replace(",", " ").split())
        )
        passwd_dict[username.strip()] = name
    return passwd_dict
