import base64
import csv
from io import StringIO
import pandas as pd
from typing import List  # will remove with 3.9

csv1 = b"""
Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKS2VlbGJ5LE1hY0NhZmZlcmt5LD
YzOTM3MTk0MzMzMjk5MjQKTGlubmVsbCxDbGVtbWV0dCwzNTU1NTg0OTI0MDkzOTU0CkVs
eXNoYSxNZWlnaGFuLDYzODU3OTU3OTM4OTcxMDYKS2F0YWxpbixFdGhlcnRvbiwzNTg0Mj
MwMDExNjgwNzAwCkZpbmEsUGFzZWssNTEwMDEzNjYzMTY2NDY4NwpBcmRlbGxhLEJyYXpp
ZXIsMjAxNzEyNjEzNjUzMzc0CkRvcnRoZWEsS2FycGluc2tpLDMwNTAyNjYxMjUxMTcyCl
Jhbm5hLER1ZmYsMzU3NjM5MzA1NjQ5MzMxMgpDaW5uYW1vbixLYWFzbWFuLDU0NDIwMjgx
NTA4MDg1NzAKSmFjbGluLFRvbmdlLDM1NDk4NTIxMDQ3MjQ1MjcK
"""
csv2 = b"""
Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKTWVsaXNlbmRhLENyb3NmaWVsZC
wzNTg0MTY2NjgwNjE3MjAzCkxpYW5hLFNlbnRlbiw2NzYyMDgzNDMwNjM3MjU2NwpEZWVy
ZHJlLE1hdGNoYW0sMzU0ODI2OTgzOTkwNDUzMwpDYXNzZXksQmxleW1hbiwzNzQ2MjI3MD
Y3OTU3OTUKRG9kaSxMZXlkb24sMzU3NTkwNDg5MzQyMjc5MgpDb25ub3IsQmVybmFyZG90
dGksMzUyODYwMjY2NDk0NDkxNQpMZXdpc3MsQnJhbnNieSw1MTAwMTM4NTUzNDQ2OTQ1Ck
p1bmllLFRhbXNldHQsMzU3MDUwNDQwNDkzMzMwNgpDb3JpbGxhLEhvZiwzMDI4NzM1NDg2
NTcyNApCb2JiaSxGZnJlbmNoLDM1NjYxMTA3Njc2NTcxNTUK
"""


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    df = pd.read_csv(StringIO(base64.b64decode(data).decode("utf-8")), sep=",")
    return list(df.credit_card.astype(str))
