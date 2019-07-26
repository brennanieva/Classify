from datastore_stuff import ToDoList

def seed_datas():
    first_input = ToDoList(user_input="Something to do")
    first_input.put()
