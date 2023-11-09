import requests

api_key = '5d7ae013-7c41-4703-8209-613600dc9974'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

defiitions = res.json()

print(defiitions)