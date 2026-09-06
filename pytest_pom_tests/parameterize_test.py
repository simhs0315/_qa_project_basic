
import pytest

@pytest.mark.parametrize(
    "number, expected",
    [
        (1, 2),
        (2, 4),
        (3, 6)
    ]
)
def test_multiply(number, expected):

    actual = number * 2

    assert actual == expected