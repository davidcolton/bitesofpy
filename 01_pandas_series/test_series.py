import series as s
import pandas as pd
import pytest
import string


def test_basic_series():
    ser = s.basic_series()
    assert isinstance(ser, pd.Series)
    assert ser.name == "Fred"
    assert ser.dtype == "int64"
    assert all(n in [1, 2, 3, 4, 5] for n in ser.values)


def test_floats_series():
    ser = s.float_series()
    assert isinstance(ser, pd.Series)
    assert ser.dtype == "float64"
    assert len(ser) == 1001
    assert ser.sum() == 500.5


def test_alpha_index_series():
    ser = s.alpha_index_series()
    assert isinstance(ser, pd.Series)
    assert len(ser) == 26
    assert sum(ser.values) == 351
    assert all(c in string.ascii_lowercase for c in ser.index)


def test_object_values_series():
    ser = s.object_values_series()
    assert isinstance(ser, pd.Series)
    assert len(ser) == 26
    assert all(c in string.ascii_uppercase for c in ser.values)
