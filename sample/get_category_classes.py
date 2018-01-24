from __future__ import print_function
from stylelens_dataset.categories import Categories
from pprint import pprint
# create an instance of the API class
api_instance = Categories()

try:
  api_response = api_instance.get_classes()
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_classes: %s\n" % e)