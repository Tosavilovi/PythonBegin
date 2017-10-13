
import requests

offset = 1 # параметр необходим для подтверждения обновления
URL = 'https://api.telegram.org/bot' # URL на который отправляется запрос
#TOKEN = '463970218:AAHWaKUtekg6sBhJKYO77_FkM8que2RV6zY' # PSnews токен вашего бота, полученный от @BotFather
TOKEN = '289062799:AAHmdbKRxqIdhnHqao6t2LjdON4jfaOiYgY' # SDM test Bot

#data = {'offset': offset, 'limit': 100, 'timeout': 0}


def get_weather(city):
    api_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
    }

    res = requests.get(api_url, params=params)
    data = res.json()
    print(data)
    if data['cod'] == '404':
        return data['message']
#        print(data['message'])
    else:
        template = "Температура в {} сейчас {} градуса(ов)"
        return template.format(city, data["main"]["temp"])
#        print(template.format(city, data["main"]["temp"]))

def check_updates(off = 1):
    data = {'offset': off,
            'limit': 100,
            'timeout': 0}
    try: # обрабатываем исключения
        request = requests.post(URL + TOKEN + '/getUpdates', data=data) # собственно сам запрос
    except:print('Error getting updates')

    if not request.status_code == 200: print('Error getting updates') # проверяем пришедший статус ответа
    if not request.json()['ok']: print('Error getting updates')

    for update in request.json()['result']:
        if off == update['update_id']:
            continue
        off = update['update_id'] #  подтверждаем текущее обновление

        if 'message' not in update or 'text' not in update['message']: # это просто текст или какая-нибудь картиночка?
            print('Unknown message')
            continue
        print(update['message']['text'])

        message_data = { # формируем информацию для отправки сообщения
            'chat_id': update['message']['chat']['id'], # куда отправляем сообщение
            'text': "<b>"+get_weather(update['message']['text'])+"</b>", # само сообщение для отправки
            'reply_to_message_id': update['message']['message_id'], # если параметр указан, то бот отправит сообщение в reply
            'parse_mode': 'HTML' # про форматирование текста ниже
        }

        try:
            request = requests.post(URL + TOKEN + '/sendMessage', data=message_data) # запрос на отправку сообщения
        except:print('Send message error')

        if not request.status_code == 200: # проверим статус пришедшего ответа
            print('Send message error')
    return  off

while True:
    try:
        offset = check_updates(offset)
    except KeyboardInterrupt: # порождается, если бота остановил пользователь
        print('Interrupted by the user')
        break