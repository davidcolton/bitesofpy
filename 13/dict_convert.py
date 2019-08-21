from collections import namedtuple
from datetime import datetime
import json


blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

Blog_NT = namedtuple(
    "Blog_NT", ["name", "founders", "started", "tags", "location", "site"]
)


def dict2nt(dict_):
    return Blog_NT(**blog)


def nt2json(nt):
    new_started = nt.started.isoformat()
    nt = nt._replace(started=new_started)
    return json.dumps(nt._asdict())
