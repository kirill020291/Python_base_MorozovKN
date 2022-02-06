from decimal import Decimal
from task_4_2 import extract_data


def currency_rates_adv(code: str) -> Decimal | None:
    """возвращает курс валюты `code` по отношению к рублю"""
    code = code.upper()
    names = extract_data("CharCode")
    if code not in names:
        return None
    index = names.index(code)
    result_value = str(extract_data('Value')[index])
    result_value = result_value.replace(',', '.')
    result_value = Decimal(result_value)
    result_value = result_value.quantize(Decimal('0.01'))
    return result_value
