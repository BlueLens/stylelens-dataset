from __future__ import print_function
from stylelens_dataset.images import Images
from pprint import pprint
# create an instance of the API class
api_instance = Images()


try:
  res = api_instance.get_images_count_by_category_name("Blouse")
  pprint(res)
except Exception as e:
  print("Exception when calling get_images_by_category_name: %s\n" % e)
