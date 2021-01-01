import os
from pathlib import Path
import string
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile

import pandas as pd

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = "311-data.zip"
    urlretrieve(f"{S3}/{data_zipfile}", TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)


_setup()

from stop_words import stop_words
from tf_idf import TFIDF


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    return pd.read_table("/tmp/samples.txt", header=0)


def strip_url_email(df_text):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    df_text["text"] = df_text["text"].str.replace(r"https?\S+|www.\S+", "", case=False)
    df_text["text"] = df_text["text"].str.replace(r"\S*@\S*", "")
    return df_text


def to_lowercase(df_text):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    df_text["text"] = df_text["text"].str.lower()
    return df_text


def strip_stopwords(df_text):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    df_text["text"] = df_text["text"].apply(
        lambda x: " ".join([token for token in x.split() if token not in stop_words])
    )
    return df_text


def strip_non_ascii(df_text):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    df_text["text"] = df_text["text"].str.encode("ascii", "ignore").str.decode("ascii")
    return df_text


def strip_digits_punctuation(df_text):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters
    df_text["text"] = df_text["text"].str.replace(r"\d+", "")
    df_text["text"] = df_text["text"].str.replace(
        r"[{}]".format(string.punctuation), ""
    )
    return df_text


def calculate_tfidf(df_text):
    # Calculate the 'tf-idf' matrix of the 'text' column
    # Return the 'tf-idf' Dataframe
    tfidf_obj = TFIDF(df_text["text"])
    return tfidf_obj()


def sort_columns(df_text):
    # Depending on how the earlier functions are implemented
    #   it's possible that the order of the columns may be different
    # Sort the 'tf-idf' Dataframe columns
    #   This ensure the tests are compatible
    df_text = df_text.sort_index(axis=1)
    return df_text


def get_tdidf():
    # Pandas’ pipeline feature allows you to string together
    #   Python functions in order to build a pipeline of data processing.
    # Complete the functions above in order to produce a 'tf-idf' Dataframe
    # Return the 'tf-idf' Dataframe
    df = (
        load_data()
        .pipe(strip_url_email)
        .pipe(to_lowercase)
        .pipe(strip_stopwords)
        .pipe(strip_non_ascii)
        .pipe(strip_digits_punctuation)
        .pipe(calculate_tfidf)
        .pipe(sort_columns)
    )
    return df
