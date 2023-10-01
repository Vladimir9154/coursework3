from datetime import datetime
from src.utils import mask_card_number, get_date, mask_account_number


def test_get_date():
    # Создаем тестовую операцию
    operation = {
        'date': '2023-09-30T10:15:00',
    }
    result = get_date(operation)
    expected = datetime(2023, 9, 30, 10, 15, 0)
    assert result == expected


def test_mask_card_number():
    card_number = '1234 5678 9012 3456'
    result = mask_card_number(card_number)
    expected = '1234 56** **** 3456'
    assert result == expected


def test_mask_account_number():
    account_number = 'Счет 1234 5678 9012 3456'
    result = mask_account_number(account_number)
    expected = 'Счет **3456'
    assert result == expected

