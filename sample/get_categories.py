from __future__ import print_function
from stylelens_dataset.categories import Categories
from pprint import pprint
# create an instance of the API class
api_instance = Categories()

try:
  offset = 0
  limit = 10

  while True:
    res = api_instance.get_categories(offset=offset, limit=limit)

    if limit > len(res):
      break
    else:
      offset = offset + limit

    pprint(res)

except Exception as e:
  print("Exception when calling add_category: %s\n" % e)
