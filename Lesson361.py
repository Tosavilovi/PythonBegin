import requests

#num = input('Enter number: ')
api_url = "http://numbersapi.com/{}/math?json=true"

with open(r"C:\DSavilov\Temp\Nums.txt", "r") as f:
    for line in f:
#        print(line)
        res = requests.get(api_url.format(line.strip()))
        data = res.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')
#        print(data['text'])
