from project import validate_transaction_date, validate_amount, validate_transaction_type, validate_currency, validate_category
from datetime import date
import pytest
########################################################################
def test_validate_transaction_date():
    assert validate_transaction_date("2026 06 26") == date(2026, 6, 26)
########################################################################
@pytest.mark.parametrize("raw", [
    "2030 06 26", "2026-06-26"
    ])
def test_validate_transaction_date(raw):
    with pytest.raises(ValueError):
        validate_transaction_date(raw)
########################################################################
@pytest.mark.parametrize("raw,expected", [
    ("+", "Income"),
    (" + ", "Income"),
    ("-", "Expense"),
    ("i+", "Investment Income"),
    ("i-", "Investment Expense"),
    ("I+", "Investment Income")
])
def test_validate_transaction_type_valid(raw, expected):
    assert validate_transaction_type(raw) == expected
########################################################################
def test_validate_transaction_type_invalid():
    with pytest.raises(ValueError):
        validate_transaction_type("o")
########################################################################
@pytest.mark.parametrize("raw,expected", [
    (" 9 ", 9.0),
    ("9", 9.0),
    ("9.8", 9.8),
    (" 9.8 ", 9.8),
])
def test_validate_amount_valid(raw, expected):
    assert validate_amount(raw) == expected
########################################################################
@pytest.mark.parametrize("raw", [
"s", "-20", "-20.1", "20,1",
])
def test_validate_amount_invalid(raw):
    with pytest.raises(ValueError):
        validate_amount(raw)
########################################################################
@pytest.mark.parametrize("raw,expected", [
    ("E", "Euro, €"),
    (" E ", "Euro, €"),
    ("e", "Euro, €"),
    (" e ", "Euro, €"),
    ("d", "Dollar, $"),
    (" d ", "Dollar, $"),
    ("D", "Dollar, $"),
    (" D ", "Dollar, $"),
])
def test_validate_currency_valid(raw, expected):
    assert validate_currency(raw) == expected
########################################################################
@pytest.mark.parametrize("raw", [
"f", "de", "2",
])
def test_validate_currency_invalid(raw):
    with pytest.raises(ValueError):
        validate_currency(raw)
########################################################################
@pytest.mark.parametrize("raw,transaction_type,expected", [
    # Income
    ("salary", "Income", "Salary"),
    ("freelance", "Income", "Freelance"),
    ("other", "Income", "Other"),
    # Expense
    ("housing", "Expense", "Housing"),
    ("food", "Expense", "Food"),
    ("transport", "Expense", "Transport"),
    ("health", "Expense", "Health"),
    ("entertainment", "Expense", "Entertainment"),
    ("education", "Expense", "Education"),
    ("clothing", "Expense", "Clothing"),
    ("subscriptions", "Expense", "Subscriptions"),
    ("other", "Expense", "Other"),
    # Investment Income
    ("savings", "Investment Income", "Savings"),
    ("stocks", "Investment Income", "Stocks"),
    ("etf", "Investment Income", "Etf"),
    ("crypto", "Investment Income", "Crypto"),
    ("other", "Investment Income", "Other"),
    # Investment Expense
    ("savings", "Investment Expense", "Savings"),
    ("other", "Investment Expense", "Other"),
    # Whitespace handling
    (" salary ", "Income", "Salary"),
    (" food ", "Expense", "Food"),
    (" stocks ", "Investment Income", "Stocks"),
    # Case insensitivity
    ("SALARY", "Income", "Salary"),
    ("FOOD", "Expense", "Food"),
    ("STOCKS", "Investment Income", "Stocks"),
])
def test_validate_category_valid(raw, transaction_type, expected):
    assert validate_category(raw, transaction_type) == expected
########################################################################
@pytest.mark.parametrize("raw,transaction_type", [
    ("whatever", "Income"),
    ("whatever", "Expense"),
    ("whatever", "Investment Income"),
    ("whatever", "Investment Expense"),
    ("salary", "Expense"),   # valid category but wrong type
    ("housing", "Income"),   # same
])
def test_validate_category_invalid(raw, transaction_type):
    with pytest.raises(ValueError):
        validate_category(raw, transaction_type)
########################################################################
