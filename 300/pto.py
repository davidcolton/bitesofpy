import calendar
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime

ERROR_MSG = (
    "Unambiguous value passed, please specify either start_month or show_workdays"
)
FEDERAL_HOLIDAYS = (
    date(2020, 9, 7),
    date(2020, 10, 12),
    date(2020, 11, 11),
    date(2020, 11, 26),
    date(2020, 12, 25),
)
WFH = (calendar.TUESDAY, calendar.WEDNESDAY)
WEEKENDS = (calendar.SATURDAY, calendar.SUNDAY)
AT_HOME = WFH + WEEKENDS


def four_day_weekend_report(df, pto):

    count_four_day_weekend = int(
        len(df["four_day_weekend"][df.four_day_weekend == True]) / 2
    )
    total_hours_all_four_day_weekend = count_four_day_weekend * 2 * 8

    title = f"{count_four_day_weekend} Four-Day Weekends"
    print_text = f"{title:^24}\n"
    print_text += f"{'=' * 24}\n"
    print_text += f"    PTO: {pto} ({int(pto / 8)} days)\n"
    print_text += f"BALANCE: {pto - total_hours_all_four_day_weekend}"
    print_text += (
        f"({abs(int((pto - total_hours_all_four_day_weekend) // 8))} days)\n\n"
    )

    mask = df["four_day_weekend_string"] != ""
    for index, row in df[mask].iterrows():
        print_text += row["four_day_weekend_string"] + row["out_of_time_marker"] + "\n"

    return print_text.strip()


def show_workdays_report(df):

    mask_hol = df["holiday"] == True
    mask_day = df["day_of_week"].str.contains(
        r"Saturday|Sunday|Tuesday|Wednesday", case=False, regex=True
    )
    mask_4dw = df["four_day_weekend"] == True
    mask = mask_hol | mask_day | mask_4dw
    df_o = df[~mask].copy()

    work_days = df_o.shape[0]

    print_text = f"Remaining Work Days: {work_days * 8} ({work_days} days) \n"
    for index, row in df_o.iterrows():
        print_text += row["date"].strftime("%Y-%m-%d") + "\n"

    return print_text.strip()


def four_day_weekends(
    *args,
    start_month: int = 8,
    paid_time_off: int = 200,
    year: int = 2020,
    show_workdays: bool = False,
) -> None:
    """Generates four day weekend report

    The four day weekends are calculated from the start_month through the end of the year
    along with the number of work days for the same time period. The reports takes into
    account any holidays that might fall within that time period and days designated as
    working from home (WFH).

    If show_workdays is set to True, a report with the work days is generated instead of
    the four day weekend dates.

    Args:
        start_month (int, optional): Month to start. Defaults to 8.
        paid_time_off (int, optional): Paid vacation days
        year (int, optional): Year to calculate, defaults to current year
        show_workdays (bool, optional): Enables work day report. Defaults to False.

    Raises:
        ValueError: ERROR_MSG
    """
    # Validate arguments
    # https://germaniumhq.com/2019/10/03/2019-10-03-Force-Named-Argument-Calling-in-Python/
    if args:
        raise ValueError(ERROR_MSG)

    # Create date Series ad seed dataframe
    first_date = datetime.strptime(f"01{start_month}{year}", "%d%m%Y").date()
    last_date = datetime.strptime(f"3112{year}", "%d%m%Y").date()
    df = pd.DataFrame({"date_time": pd.date_range(first_date, last_date)})
    df["date"] = df["date_time"].dt.date
    df["day_of_week"] = df["date_time"].dt.day_name()

    # Add holiday column and populate
    df["holiday"] = False
    for holiday in FEDERAL_HOLIDAYS:
        df.loc[df["date"] == holiday, ["holiday"]] = True

    # Identify 4 day weekends and add necessary information
    df["four_day_weekend"] = False
    df["hours_off"] = 0
    df["four_day_weekend_string"] = ""
    df["out_of_time_marker"] = ""
    friday_idx = df.index[df["day_of_week"] == "Friday"]
    monday_idx = df.index[df["day_of_week"] == "Friday"] + 3
    for friday, monday in list(zip(friday_idx, monday_idx)):
        friday_date = df["date"].iloc[friday]
        monday_date = df["date"].iloc[monday]
        date_string = (
            f'{friday_date.strftime("%Y-%m-%d")} - {monday_date.strftime("%Y-%m-%d")}'
        )
        if df["holiday"].iloc[friday] or df["holiday"].iloc[monday]:
            continue
        else:
            df.loc[df["date"] == friday_date, ["four_day_weekend"]] = True
            df.loc[df["date"] == friday_date, ["hours_off"]] = 8
            df.loc[df["date"] == friday_date, ["four_day_weekend_string"]] = date_string
            df.loc[df["date"] == monday_date, ["four_day_weekend"]] = True
            df.loc[df["date"] == monday_date, ["hours_off"]] = 8

    # Add column with reverse sum of hours off column
    # Then update four day weekend string to include *
    df["reverse_sum"] = df.loc[::-1, "hours_off"].cumsum()[::-1]
    try:
        out_of_time = (
            df["date_time"][
                (df.reverse_sum == paid_time_off) & (df.four_day_weekend == True)
            ]
            .dt.strftime("%Y-%m-%d")
            .iloc[0]
        )
        df.loc[
            df["four_day_weekend_string"].str.contains(out_of_time, na=False),
            ["out_of_time_marker"],
        ] = " *"
    except IndexError:
        pass

    if show_workdays:
        print(show_workdays_report(df))
    else:
        print(four_day_weekend_report(df, paid_time_off))

