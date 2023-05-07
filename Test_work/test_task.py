import requests


def current_price(key):
    """ Функция обрабатывает url запрос
    :return: Словарь с названием валюты и текущую цену валюты
    """
    response = requests.get(key)
    return response.json()


def determine_max_price(price):
    """
    Создает список цен равный 3000 элементам, что составляет приблизительно час наблюдений.
    Если список более 3000 элементов, то удаляет первый элемент списка
    :param price: Текущая цена валюты
    :return: Максимальное значение цены
    """
    list_price.append(price)
    if len(list_price) >= 3000:
        list_price.pop(0)
    return max(list_price)


url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
list_price = list()

while True:
    info_price = current_price(url)
    price = float(info_price['price'])
    max_price = determine_max_price(price)
    diff = abs(round(100 - (max_price/price * 100), 2))
    if diff >= 1:
        print('Цена {name} изменилась на 1% от '
              'максимальной цены - {max} за последний час'
              ' и составляет: {price}'.format(name=info_price['symbol'],
                                              max=max_price,
                                              price=price))


