import pytest
import HW11.lib as lib

random_string_generation = [
    (1, 1),
    (2.9, 2),
    (-5, 0),
    (0, 0)
]


@pytest.mark.parametrize('param, result', random_string_generation)
def test_random_string_generation(param, result):
    assert len(lib.random_string_generation(param)) == result, 'You have got error'


@pytest.mark.parametrize('param, result', random_string_generation)
def test_type_random_string_generation(param, result):
    assert type(lib.random_string_generation(param)) == str, 'You have got error'


def test_get_random_number():
    assert type(lib.get_random_number()) == float, 'You have got error'
