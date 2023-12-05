import json
from thefuzz import fuzz

# import requests
#
# API_KEY = 'AIzaSyDDqbiRfcQdH4-O7BRHgNEDER6SwFSIGG8'
# SEARCH_ENGINE_ID = '65bcfb25f936c47bb'
# document = ('Curbing dangerous climate change requires very deep cuts in emissions, as well as the use of '
#             'alternatives to fossil fuels worldwide. The good news is that countries around the globe have formally '
#             'committed—as part of the 2015 Paris Climate Agreement—to lower their emissions by setting new standards '
#             'and crafting new policies to meet or even exceed those standards. The not-so-good news is that we’re not '
#             'working fast enough. To avoid the worst impacts of climate change, scientists tell us that we need to '
#             'reduce global carbon emissions by as much as 40 percent by 2030. For that to happen, the global '
#             'community must take immediate, concrete steps: to decarbonize electricity generation by equitably '
#             'transitioning from fossil fuel–based production to renewable energy sources like wind and solar; to '
#             'electrify our cars and trucks; and to maximize energy efficiency in our buildings, appliances, '
#             'and industries.')
#
# sentences = document.split('.')
#
# total_cleaned_sentence = 0
#
# for index, sentence in enumerate(sentences):
#     if len(sentence) == 0:
#         continue
#     cleaned_sentence = sentence.strip()
#
#     total_cleaned_sentence += 1
#
#     input_file_name = 'INPUT_' + str(index) + '.json'
#     with open(input_file_name, 'w') as f:
#         f.write(cleaned_sentence)
#
# for iterator in range(total_cleaned_sentence):
#     input_file_name = 'INPUT_' + str(iterator) + '.json'
#
#     f = open(input_file_name, "r")
#     query = f.read()
#     f.close()
#
#     url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}'
#
#     response = requests.get(url)
#     data = response.json()
#
#     output_file_name = 'OUTPUT_' + str(iterator) + '.json'
#
#     with open(output_file_name, 'w') as f:
#         f.write(str(data))

with open('INPUT_0.json', 'r') as f:
    input_sentence = f.read()
    print(f.read())


# Access the search results
with open('OUTPUT_0.json', 'r') as f:
    data = json.load(f)
    for item in data.get('items', []):
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
        fuzzy_ratio = fuzz.ratio(snippet, input_sentence)
        print(f"{fuzzy_ratio} : {link}")
