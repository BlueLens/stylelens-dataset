from __future__ import print_function
from stylelens_dataset.objects import Objects
from pprint import pprint

ATTR_CLOTH_FILE = './list_attr_cloth_fabric.txt'

api_instance = Objects()

def get_attribute_clothes():
  attr_cloth = open(ATTR_CLOTH_FILE, 'r')
  attribute_clothes = []
  for pair in attr_cloth.readlines():
    map = pair.strip().rsplit(' ', 1)
    attr = {}
    attr['name'] = map[0].strip()
    attr['type'] = map[1]
    attribute_clothes.append(attr)
  return attribute_clothes


try:

  attrs = get_attribute_clothes()

  for attr in attrs:
    print(attr['name'])

    offset = 0
    limit = 100

    while True:
      res = api_instance.get_objects_by_fabric(attr['name'], offset=offset, limit=limit)
      pprint(res)
      if limit > len(res):
        break
      else:
        offset = offset + limit

except Exception as e:
  print("Exception when calling get_images_by_source: %s\n" % e)
