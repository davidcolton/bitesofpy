import re

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501

OTHER_HEADER = """
Return-Path: <info@pybit.es>
From: Bob & Julian from PyBites (info@pybit.es)
To: pybites@ninja.com
Subject: New regex learning path!
Date: Sun, 18 Aug 2019 17:16:10 -0700 (PDT)
Envelope-To: pybites@ninja.com
...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}
"""


def get_email_details(header: str) -> dict:
    """User re.search or re.match to capture the from, to, subject
       and date fields. Return the groupdict() of matching object, see:
       https://docs.python.org/3.7/library/re.html#re.Match.groupdict
       If not match, return None
    """
    pattern_dict = {
        "from": r"From: (.*)",
        "to": r"To: (.*)",
        "subject": r"Subject: (.*)",
        "date": r"Date: (.*)",
    }

    return_dict = dict()

    for key, regex in pattern_dict.items():
        try:
            res = re.findall(regex, header)[0]
        except IndexError:
            return None
        if key == "date":
            res = res[:25]
        return_dict[key] = res

    return return_dict
