from datastore_stuff import ToDoList

def seed_datas(hidden):
    input = hidden.split(",")
    print(input[0])
    print(hidden)
    ToDoList(user_input=hidden).put()
