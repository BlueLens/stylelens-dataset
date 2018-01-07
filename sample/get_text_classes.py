from __future__ import print_function
from stylelens_dataset.texts import Texts
from pprint import pprint
# create an instance of the API class
api_instance = Texts()


try:
  res = api_instance.get_classes()
  pprint(res)

except Exception as e:
  print("Exception when calling get_classes: %s\n" % e)
