import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df["Item"][df["Calories"] == df["Calories"].max()].values[0]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    # Create a mask to identify zero calorie, tea, coffee and beverages
    zero_cal = df["Calories"] == 0
    tea_coffee = df["Category"] == "Coffee & Tea"
    beverages = df["Category"] == "Beverages"
    exclude = zero_cal | tea_coffee | beverages

    # Should all drinks be excluded
    if excl_drinks == bool(True):
        df = df[~exclude]
    else:
        # Just exclude Zero Calorie Items
        df = df[~zero_cal]

    # Add the Protein / Calorie Ratio
    df["pc_ratio"] = df["Protein"] / df["Calories"]

    # Get the top 5 Protein / Calorie Ratio and Return
    top_pc_ratio = df.sort_values(by="pc_ratio", ascending=False).head(5)
    return [row["Item"] for index, row in top_pc_ratio.iterrows()]
