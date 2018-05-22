import requests
import json
import sys

query = sys.argv[1]
url = 'https://api.duckduckgo.com/?q='+ query +'&format=json&pretty=1'
resp = requests.get(url)
res = json.loads(resp.text)
result = res.get('RelatedTopics')
cell = result[0]
print(cell.get('Text'))