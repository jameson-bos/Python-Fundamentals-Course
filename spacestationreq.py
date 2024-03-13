# This script pulls JSON data from the respective API, listing the people currently in space! 

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])