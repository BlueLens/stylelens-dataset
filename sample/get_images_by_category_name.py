from __future__ import print_function
from stylelens_dataset.images import Images
from pprint import pprint
# create an instance of the API class
api_instance = Images()


try:
  offset = 0
  limit = 10

  res = api_instance.get_images_by_category_name("Blouse", offset=offset, limit=limit)
  pprint(res)
except Exception as e:
  print("Exception when calling get_images_by_category_name: %s\n" % e)
