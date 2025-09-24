import pytest

from main import calculate, parse_expression


@pytest.mark.parametrize(
    "a,op,b,expected",
    [
        (2, "+", 3, 5),
        (5, "-", 2, 3),
        (4, "*", 2.5, 10.0),
        (9, "/", 3, 3.0),
    ],
)
def test_calculate_basic(a, op, b, expected):
    assert calculate(a, op, b) == expected


def test_calculate_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(5, "/", 0)


def test_calculate_unknown_operator():
    with pytest.raises(ValueError):
        calculate(5, "%", 2)


@pytest.mark.parametrize(
    "raw,parsed",
    [
        ("2 + 3", (2.0, "+", 3.0)),
        ("  5-8", (5.0, "-", 8.0)),
        ("4 * 2.5 ", (4.0, "*", 2.5)),
        ("9/ 3", (9.0, "/", 3.0)),
    ],
)
def test_parse_expression_valid(raw, parsed):
    assert parse_expression(raw) == parsed


@pytest.mark.parametrize("raw", ["", "hello", "2 ++ 3", "2 ^ 3", "2 / 0", "2 2 +"])
def test_parse_expression_invalid(raw):
    with pytest.raises(ValueError):
        parse_expression(raw)
