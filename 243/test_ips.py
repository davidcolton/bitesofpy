import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            "13.248.118.0",
            "13.248.118.0/24 is allocated to the AMAZON service in the eu-west-1 region",
        )
    ],
)
def test_valid_ip(json_file, arg, expected):
    service_ranges = parse_ipv4_service_ranges(json_file)
    results = get_aws_service_range(arg, service_ranges)
    assert str(results[0]) == expected


@pytest.mark.parametrize("arg, expected", [("192.0.2.8", [])])
def test_empty_return(json_file, arg, expected):
    service_ranges = parse_ipv4_service_ranges(json_file)
    results = get_aws_service_range(arg, service_ranges)
    assert results == expected


def test_value_error(json_file):
    with pytest.raises(ValueError) as e:
        service_ranges = parse_ipv4_service_ranges(json_file)
        assert get_aws_service_range("260.260.260.260", service_ranges)
    assert str(e.value) == "Address must be a valid IPv4 address"
