from requests import get


def load_currency_rates():
    # Пытаемся получить актуальные курсы валют по API, в случае ошибок - используем заранее сохраненные значения
    try:
        API_KEY = '71w3HFSgPajOCUWEXyGQxIsW8AFFbAD9nVnExe2y'
        HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=EUR%2CUSD%2CRUB%2CGBP'
        currencies = get(HOST).json()['data']
        print("Актуальный курс валют загружен")
        return currencies
    except:
        currencies = {"USD": 1, "EUR": 1.08, "GBP": 1.24, "RUB": 0.012}
        print("Актуальный курс валют не загружен, используется")
        return currencies


def print_available_currencies(currencies):
    # Выводим пользователю доступный для конвертации список валют
    print("Вам предложены следующие валюты:\n")
    for currency in currencies:
        print(currency)


def get_user_currency(currencies):
    # Получаем от пользователя валюту, которую ему необходимо сконвертировать. Проверка вхождения полученного значения в словарь
    while True:
        user_currency = input("\nВведите имеющуюся валюту: ").upper()
        if user_currency in currencies:
            return user_currency
        else:
            print("Некорректная валюта. Пожалуйста, выберите из списка предложенных валют.")


def get_amount():
    # Получаем от пользователя количество конвертируемой валюты. Проверка типа данных полученного значения + проверка на отрицательные и нулевые значения
    while True:
        try:
            amount = float(input("Введите имеющуюся сумму: "))
            if amount > 0:
                return amount
            else:
                print("Некорректная сумма. Пожалуйста, введите положительное значение.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числовое значение.")


def get_conversion_currency(currencies):
    # Получаем от пользователя валюту, в которую ему необходимо сконвертировать. Проверка вхождения полученного значения в словарь
    while True:
        conversion_currency = input("Выберите валюту для конвертации: ").upper()
        if conversion_currency in currencies:
            return conversion_currency
        else:
            print("Некорректная валюта. Пожалуйста, выберите из предложенных валют.")


def convert_currency(user_currency, conversion_currency, amount, currencies):
    # Конвертирует валюту на основании полученных от пользователя данных и возвращает результат
    converted_amount = amount / currencies[user_currency] * currencies[conversion_currency]
    return round(converted_amount, 2)


print("""
Добро пожаловать в конвертер валют!

Наша программа поможет Вам конвертировать валюту.
- Ввод имеющейся валюты
- Ввод суммы этой валюты
- Выбор валюты для конвертации
""")

CURRENCIES = load_currency_rates()
print_available_currencies(CURRENCIES)

user_currency = get_user_currency(CURRENCIES)
current_amount = get_amount()
conversion_currency = get_conversion_currency(CURRENCIES)

converted_amount = convert_currency(user_currency, conversion_currency, current_amount, CURRENCIES)
print(f"Итого: {converted_amount} {conversion_currency}")
