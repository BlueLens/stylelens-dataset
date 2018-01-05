from __future__ import print_function
from stylelens_dataset.colors import Colors
from pprint import pprint
# create an instance of the API class
api_instance = Colors()

color = {}
color['file'] = 'xxx.jpg'
color['name'] = 'red'
color['code'] = '1'

try:
  api_response = api_instance.add_color(color)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_color: %s\n" % e)
