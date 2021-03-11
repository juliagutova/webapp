from flask import current_app
import requests


def weather_by_city(city_name): # функция которая принимает название города
    weather_url = current_app.config['WETHER_URL']
    params = { # передаем все параметры с помощью словаря. все строки, кроме city_name - переменная которая приходит из вне
        'key': current_app.config['WETHER_API_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru',
    }
    try:
        result = requests.get(weather_url, params=params) # URL, ответ сервера, тело запроса, заголовки вернется в result
        result.raise_for_status() #Обрабатываем ошибки если код 400 или 500
        weather = result.json() # преобразуем в вид питоновского словаря
        if 'data' in weather: # функция будет возв. либо погодные данные либо False
            if 'current_condition' in weather['data']:
                try: 
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError): # выдает ошибку в случае отсутствия интернета, неправильного адреса
        print('Сетевая ошибка')
        return False 
    return False

if __name__ == '__main__':
    print(weather_by_city('Moscow,Russia'))
    