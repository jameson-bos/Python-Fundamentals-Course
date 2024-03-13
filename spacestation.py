# This script pulls JSON data from the respective API, listing the people currently in space! 

import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])

# Uninstalled requests in Terminal
# To run this code, install requests globally from Terminal                 You can also use a virtual environment with requests installed to run program
    # 'pip3 install requests'                                               Do this with View > Command Pallete > Select Interpretor > Find venv
#                                                                          To deactivate, run deactivate in terminal