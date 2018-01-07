from __future__ import print_function
from stylelens_dataset.colors import Colors
from pprint import pprint
# create an instance of the API class
api_instance = Colors()

try:
  api_response = api_instance.get_classes()
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_color_classes: %s\n" % e)
