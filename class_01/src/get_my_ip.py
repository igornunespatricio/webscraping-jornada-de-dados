import requests

url = "http://lumtest.com/myip.json"
url = "http://www.globo.com"
response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to fetch IP address. Status code: {response.status_code}")

print(response.json())
