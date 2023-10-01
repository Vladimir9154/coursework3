import json
from datetime import datetime


def filter_operations(operations_data):
    """Фильтрация операций"""
    executed_operations = []
    for operation in operations_data:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations


def load_operations_data(operations_path):
    """Загрузка данных из файла operations.json"""
    with open(operations_path, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
        return operations_data


def get_date(operation_):
    """Извлекает даты из операции"""
    return datetime.fromisoformat(operation_['date'])


def mask_card_number(card_number):
    """"Маскировка номера карты"""
    parts = card_number.split()
    masked_parts = []

    for part in parts:
        if part.isdigit():
            masked_part = part[:4] + ' ' + part[4:6] + '** **** ' + part[-4:]
        else:
            masked_part = part
        masked_parts.append(masked_part)

    return ' '.join(masked_parts)


def mask_account_number(account_number):
    """Маскировка номера счета"""
    parts = account_number.split()
    masked_parts = []
    for part in parts:
        if part.isdigit():
            masked_part = '**' + part[-4:]
        else:
            masked_part = part
        masked_parts.append(masked_part)
    return ' '.join(masked_parts)


def sort_operations(executed_operations):
    """Сортировка операций по датам"""
    executed_operations.sort(key=get_date, reverse=True)


def show_last_5_operations_info(last_5_operations):
    for operation in last_5_operations:
        date = datetime.fromisoformat(operation['date']).strftime('%d.%m.%Y')
        description = operation['description']
        # Значение поля 'from'
        from_value = operation.get('from', '')
        # Значение поля 'to'
        to_value = operation['to']

        # Определяем, является ли 'from' номером счета или номером карты
        if from_value.startswith('Счет'):
            from_account = mask_account_number(from_value)
        else:
            from_account = mask_card_number(from_value)

        # Определяем, является ли 'to' номером счета или номером карты
        if to_value.startswith('Счет'):
            to_account = mask_account_number(to_value)
        else:
            to_account = mask_card_number(to_value)
        amount = float(operation['operationAmount']['amount'])
        currency = operation['operationAmount']['currency']['name']

        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"{amount} {currency}\n")
