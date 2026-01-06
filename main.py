todos = []

def get_todos():
    with open(f"todos.txt", "r") as file_local:
        local_todos = file_local.readlines()
    return local_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif user_action.startswith("show"):

        todos = get_todos()

        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip("\n")}")


    elif user_action.startswith("edit"):

        try:
            index = int(user_action[5:])
            index -= 1

            todos = get_todos()

            todo_to_change = todos[index]

            new_todo = input("Enter new todo:")
            todos[index] = new_todo + "\n"

            with open(f"todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {todo_to_change.strip("\n")} has been changed to {new_todo}")

        except ValueError:
            print("Invalid command! Syntax for Edit Command is edit <index of list to be changed>")
            continue
        except IndexError:
            print("Invalid Index Number! Please enter a valid index")
            continue

    elif user_action.startswith("complete"):

        try:
            todos = get_todos()

            index = int(user_action[9:]) -1
            todos.pop(index)

            with open(f"todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid command! Syntax for Edit Command is edit <index of list to be changed>")
            continue
        except IndexError:
            print("Invalid Index Number! Please enter a valid index")
            continue


    elif user_action.startswith("exit"):
        break


    else:
        print("Invalid input")
        continue

print ("Goodbye")