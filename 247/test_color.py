from unittest.mock import patch
from random import sample
import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@patch("color.sample")
def test_gen_hex_color(patched_sample, gen):
    patched_sample.return_value = [37, 109, 122]
    assert next(gen) == "#256D7A"
    patched_sample.assert_called_with(range(0, 256), 3)


@patch("color.sample")
def test_value_error(patched_sample, gen):
    patched_sample.return_value = [37, 109, 122, 0]
    with pytest.raises(ValueError) as e:
        assert next(gen)

