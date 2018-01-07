from __future__ import print_function
from stylelens_dataset.texts import Texts
from pprint import pprint
# create an instance of the API class
api_instance = Texts()


try:
  offset = 0
  limit = 5
  class_code = "1"

  while True:
    res = api_instance.get_texts_by_class_code(class_code, offset=offset, limit=limit)

    pprint(res)
    if limit >= len(res):
      break
    else:
      offset = offset + limit

except Exception as e:
  print("Exception when calling get_texts_by_class_code: %s\n" % e)
