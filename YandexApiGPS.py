import requests

city = input('Введите город: ')
api_url = " https://geocode-maps.yandex.ru/1.x/?format=json&geocode={}"

#with open(r"C:\DSavilov\Temp\Nums.txt", "r") as f:
#    for line in f:
#        print(line)
#        res = requests.get(api_url.format(line.strip()))
res = requests.get(api_url.format(city.strip()))
data = res.json()['response']

for key in data:
    print(key,' : ', data[key])