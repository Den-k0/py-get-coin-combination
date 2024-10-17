import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_cents, output_result",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ],
    ids=[
        "return only pennies",
        "return only nickels",
        "return only dimes",
        "return only quarters",
    ]
)
def test_coin_combination(
        input_cents: int,
        output_result: list[int, int, int, int]
) -> None:
    assert get_coin_combination(input_cents) == output_result
