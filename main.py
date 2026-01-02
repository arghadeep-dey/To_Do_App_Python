todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if "add" in user_action:

        todo = user_action[4:]

        with open(f"todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif "show" in user_action:

        with open(f"todos.txt", "r") as file:
            todos = file.readlines()

        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip("\n")}")


    elif "edit" in user_action:

        index = int(user_action[5:])
        index -= 1

        with open(f"todos.txt", "r") as file:
            todos = file.readlines()

        todo_to_change = todos[index]

        new_todo = input("Enter new todo:")
        todos[index] = new_todo + "\n"

        with open(f"todos.txt", "w") as file:
            file.writelines(todos)

        print(f"Todo {todo_to_change.strip("\n")} has been changed to {new_todo}")


    elif "complete" in user_action:
        with open(f"todos.txt", "r") as file:
            todos = file.readlines()

        index = int(user_action[9:]) -1
        todos.pop(index)

        with open(f"todos.txt", "w") as file:
            file.writelines(todos)


    elif "exit" in user_action:
        break


    else:
        print("Invalid input")
        continue

print ("Goodbye")