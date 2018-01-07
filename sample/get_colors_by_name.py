from __future__ import print_function
from stylelens_dataset.colors import Colors
from pprint import pprint
# create an instance of the API class
api_instance = Colors()

try:
  classes = api_instance.get_classes()
  for clazz in classes:
    pprint('code: ' + clazz['code'])
    pprint('name: ' + clazz['name'])
    pprint('value: ' + clazz['value'])
    while True:
      offset = 0
      limit = 100
      i = 0
      colors = api_instance.get_colors_by_name(clazz['name'], offset=offset, limit=limit)

      for color in colors:
        pprint(color)
      if limit > len(colors):
        break
      else:
        offset = offset + limit
      i = i + 1
      print(i)

except Exception as e:
  print("Exception when calling get_colors_by_name: %s\n" % e)
