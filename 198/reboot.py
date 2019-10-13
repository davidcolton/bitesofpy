from dateutil.parser import parse
import datetime

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    # Split into list, filter empty, extract date and sort
    lines = list(filter(None, reboots.splitlines()))
    dates = sorted([parse(x.split("~")[1].strip()) for x in lines])

    # A list to hold the uptime tuples
    list_of_uptimes = []

    # The first reboot date time
    reboot = dates[0]

    # Iterate over the remaining reboots added tuples of
    # The days since last reboot and the date of this reboot
    for next_reboot in dates[1:]:
        uptime = (next_reboot - reboot).days
        list_of_uptimes.append((uptime, next_reboot.strftime("%Y-%m-%d")))
        reboot = next_reboot

    # Return the tuple of the max days
    return max(list_of_uptimes)

