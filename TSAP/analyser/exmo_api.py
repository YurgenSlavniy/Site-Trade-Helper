import requests

response = requests.post("https://api.exmo.com/v1.1/trades")
print(response.text)