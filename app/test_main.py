from app.main import outdated_products
import datetime
import pytest
from unittest import mock


@pytest.fixture()
def products_template():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "date,expected",
    [
        (datetime.date(2022, 2, 3), ["duck"]),
        (datetime.date(2022, 2, 9), ["chicken", "duck"]),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
@mock.patch("app.main.datetime")
def test_outdated_products(mock_datetime, products_template, date, expected):
    mock_datetime.date.today.return_value = date
    assert outdated_products(products_template) == expected
