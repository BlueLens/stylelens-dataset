from __future__ import print_function
from stylelens_dataset.texts import Texts
from pprint import pprint
# create an instance of the API class
api_instance = Texts()

try:
  text = {}
  text['class_code'] = '1'
  text['text'] = 'test'

  api_response = api_instance.add_text(text)
  pprint(api_response)

except Exception as e:
  print("Exception when calling add_text: %s\n" % e)