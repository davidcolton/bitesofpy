from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


# define exception classes here
class UserDoesNotExist(Exception):
    """Exception when the user does not exist."""

    pass


class UserAccessExpired(Exception):
    """Exception when the users access has expired."""

    pass


class UserNoPermission(Exception):
    """Exception when the users has no permission."""

    pass


def get_secret_token(username):
    # Does the user exist
    if not any(user.name == username for user in USERS):
        raise UserDoesNotExist

    # The user exists so get it
    for user in USERS:
        if user.name == username:
            if user.expired:
                raise UserAccessExpired
            elif user.role == USER:
                raise UserNoPermission
            else:
                return SECRET
