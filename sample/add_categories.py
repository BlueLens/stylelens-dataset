from __future__ import print_function
from stylelens_dataset.categories import Categories
from pprint import pprint
# create an instance of the API class
api_instance = Categories()

try:
  category = {}
  category['name'] = 'test_name'
  category['class_code'] = '1'

  api_response = api_instance.add_category(category)
  pprint(api_response)

except Exception as e:
  print("Exception when calling add_category: %s\n" % e)