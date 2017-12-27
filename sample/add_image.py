from __future__ import print_function
from stylelens_dataset.images import Images
from pprint import pprint
# create an instance of the API class
api_instance = Images()

image = {}
image['file'] = "xxxkkkx"
image['source'] = 'deepfashion'

size = {}
size['width'] = 300
size['height'] = 500
size['depth'] = 3

objects = []
object = {}
box = {}
box['x1'] = 10.0
box['y1'] = 10.0
box['x2'] = 40.0
box['y2'] = 60.0
object['name'] = 'xxx'
object['box'] = box
objects.append(object)

image['size'] = size
image['objects'] = objects

try:
  api_response = api_instance.add_image(image)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->add_object: %s\n" % e)
