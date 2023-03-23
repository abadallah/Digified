import requests

URL = "http://localhost:8000"

name = "احمد محمد محمود"

PARAMS = {'name':name}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
print(data)