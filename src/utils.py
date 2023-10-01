from datetime import datetime


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
