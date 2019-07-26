from google.appengine.ext import ndb

# One to One
class ToDoList(ndb.Model):
    user_input = ndb.StringProperty(required=True)
