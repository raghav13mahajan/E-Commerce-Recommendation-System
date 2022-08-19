import json
from pprint import pprint

with open('new_oo.json') as data_file:    
    data = json.load(data_file)

pprint(data)
