from __future__ import print_function
from stylelens_dataset.images import Images
from pprint import pprint
# create an instance of the API class
api_instance = Images()


try:
  offset = 0
  limit = 100

  while True:
    res = api_instance.get_images_by_category_class("1", offset=offset, limit=limit)

    pprint(res)
    if limit > len(res):
      break
    else:
      offset = offset + limit

except Exception as e:
  print("Exception when calling get_images_by_source: %s\n" % e)
