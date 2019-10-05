from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join("/tmp", "course_timings")
urllib.request.urlretrieve("http://bit.ly/2Eb0iQF", COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    pattern = re.compile(r"Start.*\((\d{1,2}:\d{2})\)")
    with open(COURSE_TIMES, "r") as f:
        return pattern.findall(f.read())


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total_time = timedelta(seconds=0)
    for video_time in timestamps:
        mins, secs = video_time.split(":")
        total_time += timedelta(minutes=int(mins), seconds=int(secs))
    return str(total_time)
