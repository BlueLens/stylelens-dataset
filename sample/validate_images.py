from __future__ import print_function
from stylelens_dataset.images import Images
from pprint import pprint
# create an instance of the API class
api_instance = Images()


try:
  ids = []

  ids.append('5a718ce0bd44107fbae98994')

  res = api_instance.validate_images(ids, valid=True)
  pprint(res)
except Exception as e:
  print("Exception when calling validate_images: %s\n" % e)
