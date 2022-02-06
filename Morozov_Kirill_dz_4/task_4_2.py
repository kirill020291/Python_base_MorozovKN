from decimal import Decimal
import lxml
import requests
import sys
import typing
from pyquery import PyQuery as pq
from lxml import etree

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def send_request() -> requests.Response:
    """Выполняет запрос данных с ЦБР"""
    response = requests.get(URL, timeout=2)
    if not response.ok:
        print(f'Запрос не успешен: {response.status_code}')
        sys.exit(0)
    return response


def extract_data(tag: str) -> typing.List:
    """Извлекает данные из соответствующего тега и возвращает список string значений"""
    res = send_request()
    main_root = pq(lxml.etree.fromstring(res.content))
    curs_val = main_root.pop()
    return curs_val.xpath(f'//Valute/{tag}/text()')


def currency_rates(code: str) -> Decimal | None:
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


if __name__ == '__main__':
    print(currency_rates("eUr"))
    print(currency_rates("noname"))
