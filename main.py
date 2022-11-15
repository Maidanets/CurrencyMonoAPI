import requests
import time
import csv
from pprint import pprint
from API_TXT.txt_from_api import txt_file_from_api
from API_JSON.json_from_api import json_file_from_api
from API_CSV.csv_from_api import csv_file_from_api


# exchange_rate = response_API()
# api_in_txt = txt_file_from_api(exchange_rate)
# api_in_json = json_file_from_api(exchange_rate)
# api_in_csv = csv_file_from_api(exchange_rate)

class CurrencyMonoAPI:
    __url = "https://api.monobank.ua/bank/currency"  # Зробив приватним, томущо його використовує тільки внутрішня функція

    def response_API(self):
        response = requests.get(self.__url)
        return response.json()


class CurrencyMono:
    inputCode = None
    currencyCodeA = None
    currencyCodeB = None
    date = None
    rateSell = None
    rateBuy = None
    rateCross = None

    def __init__(self, input_code):
        CurrencyMonoAPI()
        try:
            if input_code.isnumeric():
                self.inputCode = int(input_code)
                self.currency()
            elif input_code.isalpha():
                self.inputCode = int(Converter().converter_ISO_4217(input_code))
                self.currency()
            else:
                print("Invalid value, try again.")
        except Exception:
            print("Invalid value, try again.")

    def currency(self, response_currency=CurrencyMonoAPI().response_API()):
        try:
            for i in response_currency:
                if (i.get('currencyCodeA')) == self.inputCode:
                    CurrencyMono.currencyCodeA = Converter().converter_ISO_4217(str(i.get('currencyCodeA')))
                    CurrencyMono.currencyCodeB = Converter().converter_ISO_4217(str(i.get('currencyCodeB')))
                    CurrencyMono.date = Converter().converter_unix_time(i.get('date'))
                    CurrencyMono.rateSell = i.get('rateSell')
                    CurrencyMono.rateBuy = i.get('rateBuy')
                    CurrencyMono.rateCross = i.get('rateCross')

        except Exception:
            print("Please try again later, many requests.")  # помилка через часті запити до API
        else:
            self.__currency_print()

        return self.currencyCodeA, self.currencyCodeB, self.date, self.rateBuy, self.rateSell, self.rateCross

    # Зробив приватною, бо сама по собі функція нічого не виводить, вона працює тільки в парі з попередньою
    def __currency_print(self):
        if self.rateCross is None and self.currencyCodeA is not None:
            print(f"Currency Code 1: {self.currencyCodeA}\n"
                  f"Currency Code 2: {self.currencyCodeB}\n"
                  f"Sell: {self.rateSell}\n"
                  f"Buy: {self.rateBuy}\n"
                  f"Date: {self.date}\n")
        elif self.currencyCodeA is not None:
            print(f"Currency Code 1: {self.currencyCodeA}\n"
                  f"Currency Code 2: {self.currencyCodeB}\n"
                  f"Cross: {self.rateCross}\n"
                  f"Date: {self.date}\n")
        else:
            print("Unfortunately, there are no values for this currency.")


# Список кодів валют
class CurrencyCodes:
    currency_codes_list = []

    def __init__(self):
        with open('CurrencyCodes/CurrencyCodes.csv', mode='r') as currency_codes_csv:
            currency_codes = csv.reader(currency_codes_csv)
            for i in currency_codes:
                self.currency_codes_list.append(i[0].split(';'))


# Конвертер значень
class Converter:

    # Переводить час з секунд в звичайний формат
    def converter_unix_time(self, unix_time):
        return time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime(unix_time))

    # Переводить числовий код в текстовий і навпаки
    def converter_ISO_4217(self, code_iso_4217):
        for i in CurrencyCodes().currency_codes_list:
            if code_iso_4217 == i[1]:
                return i[0]
            elif code_iso_4217 == i[0]:
                return i[1]


# Значення 1
currency_USD = CurrencyMono('USD')  # USD або 840

# Значення 2
currency_EUR = CurrencyMono('978')  # EUR або 978

# Значення 3
currency_code = CurrencyMono(input("Enter currency code: ").upper())  # Код у форматі 840 або USD

# Значення 4
converter_code_UAH = Converter().converter_ISO_4217('980')
print(f"Код 980 = {converter_code_UAH}")

# Значення 5
converter_code_980 = Converter().converter_ISO_4217('UAH')
print(f"Код UAH = {converter_code_980}")

# Значення 6
input_converter_code = input("Введіть код який бажаєте конвертувати: ").upper()  # Код у форматі 840 або USD
converter_code = Converter().converter_ISO_4217(input_converter_code)
print(f"Ваш код {input_converter_code} = {converter_code}")




