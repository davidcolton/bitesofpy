import pandas as pd
from io import StringIO
import json

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com  
"""


def convert_to_json(members=members):
    df = pd.read_csv(StringIO(members), sep="[;,|]", engine="python")
    df.id = df.id.astype(str)
    return df.to_json(orient="records")

    """
    d = [
        dict([(colname, row[i]) for i, colname in enumerate(df.columns)])
        for row in df.values
    ]

    return json.dumps(d)"""