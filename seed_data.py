from datastore_stuff import ToDoList

def seed_datas(hidden):
    input = hidden.split(",")
    print("This is the input " + str(input))
    # print(input[0])
    # print(hidden)
    todo = ToDoList()
    for task in input:
        todo.user_input.append(task)


    todo.put()
    print("Array of user tasks: "+ str(todo))
