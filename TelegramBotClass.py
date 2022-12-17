import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Не возможно перевести одинаковые валюты {quote}!')

        try:
            quote_ticer = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработаь валюту {quote}!')

        try:
            base_ticer = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработаь валюту {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticer}&tsyms={base_ticer}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base