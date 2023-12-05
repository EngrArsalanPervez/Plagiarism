from thefuzz import fuzz
import requests

API_KEY = 'AIzaSyDDqbiRfcQdH4-O7BRHgNEDER6SwFSIGG8'
SEARCH_ENGINE_ID = '65bcfb25f936c47bb'
document = ('Curbing dangerous climate change requires very deep cuts in emissions, as well as the use of '
            'alternatives to fossil fuels worldwide. The good news is that countries around the globe have formally '
            'committed—as part of the 2015 Paris Climate Agreement—to lower their emissions by setting new standards '
            'and crafting new policies to meet or even exceed those standards. The not-so-good news is that we’re not '
            'working fast enough. To avoid the worst impacts of climate change, scientists tell us that we need to '
            'reduce global carbon emissions by as much as 40 percent by 2030. For that to happen, the global '
            'community must take immediate, concrete steps: to decarbonize electricity generation by equitably '
            'transitioning from fossil fuel–based production to renewable energy sources like wind and solar; to '
            'electrify our cars and trucks; and to maximize energy efficiency in our buildings, appliances, '
            'and industries.')


url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={document}'

response = requests.get(url)
data = response.json()

with open("DATA.JSON", 'w') as f:
    f.write(str(data))

print(f'\n\n{document}')

for item in data.get('items', []):
    fuzzy_ratio = fuzz.ratio(item.get('snippet'), document)
    print(f"{fuzzy_ratio} : {item.get('link')}")


sentences = document.split('.')


for index, sentence in enumerate(sentences):
    if len(sentence) == 0:
        continue

    query = sentence.strip()

    url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}'

    response = requests.get(url)
    data = response.json()

    print(f'\n\n{index} - {query}')

    for item in data.get('items', []):
        fuzzy_ratio = fuzz.ratio(item.get('snippet'), query)
        print(f"{fuzzy_ratio} : {item.get('link')}")