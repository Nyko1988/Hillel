import pytest
import lib
from exceptiongroup import ExceptionGroup

test_get_random_number= [
    (0.1, 0.2, 0.3),
    (5, 6, 11),
    (0, 0, 0),
]

#def test_random_string_generation():
#    assert type(lib.random_string_generation()) == str
@pytest.mark.parametrize('expected', test_get_random_number)
def test_get_random_number(expected):
    assert type(lib.get_random_number()) == float


