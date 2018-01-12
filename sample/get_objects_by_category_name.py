from __future__ import print_function
from stylelens_dataset.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  offset = 0
  limit = 100

  while True:
    res = api_instance.get_objects_by_category_name("Blouse", offset=offset, limit=limit)

    pprint(res)
    if limit > len(res):
      break
    else:
      offset = offset + limit

except Exception as e:
  print("Exception when calling get_objects_by_category_name: %s\n" % e)
