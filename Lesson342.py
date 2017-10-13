import re
import requests

res = requests.get("ftp://ftp.crystals.ru/test/test.html")
print(res.status_code)
print(res.headers)