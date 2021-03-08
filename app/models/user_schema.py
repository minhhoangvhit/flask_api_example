from app.factory.validation import Validator
from app.factory.database import Database

class User(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.collection_name = 'User'
        self.fields = {
            "name" : 'string',
            "email" :'string',
            "phone" : "string",
            "country" : "string"
        }

    def create(self, user):
        res = self.db.insert(user, self.collection_name)
        return "Inserted Id: " + res

    def find(self, user):  # find all
        return self.db.find(user, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, user):
        """ self.validator.validate(todo, self.fields, self.update_required_fields, self.update_optional_fields) """
        return self.db.update(id, user, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)