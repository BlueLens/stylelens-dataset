from __future__ import print_function
from stylelens_dataset.images import Images
from pprint import pprint
# create an instance of the API class
api_instance = Images()


try:
  api_response = api_instance.get_images_by_source("deepfashion")
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_images_by_source: %s\n" % e)
