from utils import load_operations_data, filter_operations, sort_operations, \
    show_last_5_operations_info

# указываем путь к операциям
operations_path = '../data/operations.json'

# Загрузка данных из файла operations.json
operations_data = load_operations_data(operations_path)

# Фильтрация операций
executed_operations = filter_operations(operations_data)

# Сортировка операций по дате
sort_operations(executed_operations)

# Выбор последних 5 операций
last_5_operations = executed_operations[:5]


# Вывод информации о последних операциях
show_last_5_operations_info(last_5_operations)
