import json
from datetime import datetime
from utils import get_date, mask_card_number, mask_account_number

# Загрузка данных из файла operations.json
with open('operations.json', 'r', encoding='utf-8') as file:
    operations_data = json.load(file)

# Фильтрация операций
executed_operations = []
for operation in operations_data:
    if operation.get('state') == 'EXECUTED':
        executed_operations.append(operation)


# Сортировка операций по дате
executed_operations.sort(key=get_date, reverse=True)

# Выбор последних 5 операций
last_5_operations = executed_operations[:5]


# Вывод информации о последних операциях
for operation in last_5_operations:
    date = datetime.fromisoformat(operation['date']).strftime('%d.%m.%Y')
    description = operation['description']
    from_value = operation.get('from', '')  # Значение поля 'from'
    to_value = operation['to']  # Значение поля 'to'

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
