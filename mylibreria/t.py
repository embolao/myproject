from typing import NamedTuple
import pytest


class Case(NamedTuple):
    input_x: int
    expected: int


def square(n: int) -> int:
    """docstring for square"""
    return n * n


@pytest.mark.parametrize(
    ('input_x', 'expected'),
    (
        (1, 1),
        pytest.param(-1, 1, id='negative_trivial_case'),
        Case(input_x=2, expected=4),
        (-2, 4),
    ),
)
def test_square(input_x, expected):
    """docstring for test_square"""
    assert square(input_x) == expected


@pytest.mark.parametrize(
    'input_x',
    (
        'a',
        [],
        (),
    ),
)
def test_square_error(input_x):
    """docstring for test_square_error"""
    with pytest.raises(TypeError):
        square(input_x)
