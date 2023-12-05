import requests

API_KEY = 'AIzaSyDDqbiRfcQdH4-O7BRHgNEDER6SwFSIGG8'
SEARCH_ENGINE_ID = '65bcfb25f936c47bb'
with open('document.txt', 'r') as f:
    document = f.read()


url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={document}'

response = requests.get(url)
data = response.json()

with open("links.txt", 'w') as f:
    for item in data.get('items', []):
        f.write(item.get('link') + '\n')
