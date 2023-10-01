import pytest
from datetime import datetime
from src.utils import mask_card_number, get_date, mask_account_number, \
    filter_operations, load_operations_data, show_last_5_operations_info, \
    sort_operations


# тест фильтрации операций
def test_filter_operations():
    operations_data = [
        {"id": 594226727, "state": "CANCELED",
         "date": "2018-09-12T21:27:25.241689",
         "operationAmount": {"amount": "67314.70",
                             "currency": {"name": "руб.",
                                          "code": "RUB"}},
         "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588",
         "to": "Счет 14211924144426031657"},
        {"id": 594888887, "state": "EXECUTED",
         "date": "2019-12-08T22:46:21.935582",
         "operationAmount": {"amount": "41096.24",
                             "currency": {"name": "руб.",
                                          "code": "RUB"}},
         "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588",
         "to": "Счет 14211924144426031657"}
    ]
    result = filter_operations(operations_data)
    expected = [
        {"id": 594888887, "state": "EXECUTED",
         "date": "2019-12-08T22:46:21.935582",
         "operationAmount": {"amount": "41096.24",
                             "currency": {"name": "руб.",
                                          "code": "RUB"}},
         "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588",
         "to": "Счет 14211924144426031657"}
    ]
    assert result == expected


# тест получения даты из операции
def test_get_date():
    operation = {
        "date": "2019-08-26T10:50:58",
    }
    result = get_date(operation)
    expected = datetime(2019, 8, 26, 10, 50, 58)
    assert result == expected


# тест маскировки номера карты
def test_mask_card_number():
    card_number = "MasterCard 7158300734726758"
    result = mask_card_number(card_number)
    expected = 'MasterCard 7158 30** **** 6758'
    assert result == expected


# тест маскировки номера счета
def test_mask_account_number():
    account_number = 'Счет 35383033474447895560'
    result = mask_account_number(account_number)
    expected = 'Счет **5560'
    assert result == expected


# тест загрузки операций
def test_load_operations_data():
    operations_path = '../tests/data/test_operations.json'
    result = load_operations_data(operations_path)
    expected = [
        {
            "id": 716496732, "state": "EXECUTED", "date":
            "2018-04-04T17:33:34.701093", "operationAmount":
            {"amount": "40701.91", "currency":
                {"name": "USD", "code": "USD"}},
            "description": "Перевод организации", "from":
            "Visa Gold 5999414228426353", "to": "Счет 72731966109147704472"
        }
    ]
    assert result == expected


def test_sort_operations():
    # Создаем тестовые данные
    operations = [
        {'date': '2023-09-30T10:15:00'},
        {'date': '2023-09-29T08:30:00'},
        {'date': '2023-09-28T14:45:00'},
    ]
    # Ожидаем, что операции будут отсортированы в обратном порядке
    expected_dates = [
        datetime(2023, 9, 30, 10, 15, 0),
        datetime(2023, 9, 29, 8, 30, 0),
        datetime(2023, 9, 28, 14, 45, 0),
    ]

    sort_operations(operations)

    for i, operation in enumerate(operations):
        assert get_date(operation) == expected_dates[i]


#
# def test_show_last_5_operations_info():
#     # указываем путь к операциям
#     operations_path = '../data/operations.json'
#
#     # Загрузка данных из файла operations.json
#     operations_data = load_operations_data(operations_path)
#
#     # Фильтрация операций
#     executed_operations = filter_operations(operations_data)
#
#     # Сортировка операций по дате
#     sort_operations(executed_operations)
#
#     # Выбор последних 5 операций
#     last_5_operations = executed_operations[:5]
#
#     result = show_last_5_operations_info(last_5_operations)
#
#     expected = None
#     assert result == expected
