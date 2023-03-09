import pytest

from .lib import Phone, Laptop


@pytest.fixture(scope='class')
def phone():
    phone_data = Phone(
        producer='Samsung',
        year_of_development=2015,
        gsm_modem=True,
        activated=True

    )
    yield phone_data


@pytest.fixture(scope='class')
def laptop():
    laptop_data = Laptop(
        producer='Samsung',
        year_of_development=2020,
        gsm_modem=True,
        battery_is_arranged=True
    )
    yield laptop_data
