from stylelens_dataset.database import DataBase

class Categories(DataBase):
  def __init__(self):
    super(Categories, self).__init__()
    self.categories = self.db.categories
    self.classes = self.db.categori_classes

  def add_category(self, category):
    id = None
    query = {"name": category["name"],
             "class_code": category["class_code"]}
    try:
      r = self.categories.update_one(query, {"$set": category},
                                upsert=True)
    except Exception as e:
      print(e)

    if 'upserted' in r.raw_result:
      id = str(r.raw_result['upserted'])

    return id