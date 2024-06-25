#creating a to do list
todolist = []
print("Welcome to the To Do List app")
print("This was created by Mohammed Sanusi")
while True:
    usertodo = input("Type in what you're doing today (type quit to end the list): ")
    if usertodo !=  "quit":
        todolist.append(usertodo)
        continue
    elif usertodo == "quit":
        print("Here is your to do list: ")
        print(todolist)
        break
    else:
        continue
print("©mohtech")
