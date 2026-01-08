todos = []

def get_todos(filepath):
    with open(filepath, "r") as file_local:
        local_todos = file_local.readlines()
    return local_todos

def write_todos(filepath,todos_arg):
    try:
        with open(filepath, "w") as file_local:
            file_local.writelines(todos_arg)
        return 1
    except FileNotFoundError:
        print(f"{filepath} does not exist")
        return 0

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        write_todos(f"todos.txt",todos)

        print(f"{user_action[4:]} has been Added!")


    elif user_action.startswith("show"):
        print("Showing all todos with their respective indexes")
        todos = get_todos("todos.txt")

        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip("\n")}")


    elif user_action.startswith("edit"):

        try:
            index = int(user_action[5:])
            index -= 1

            todos = get_todos("todos.txt")

            todo_to_change = todos[index]

            new_todo = input("Enter new todo:")
            todos[index] = new_todo + "\n"

            write_todos(f"todos.txt",todos)

            print(f"Todo {todo_to_change.strip("\n")} has been changed to {new_todo}")

        except ValueError:
            print("Invalid command! Syntax for Edit Command is edit <index of list to be changed>")
            continue
        except IndexError:
            print("Invalid Index Number! Please enter a valid index")
            continue

    elif user_action.startswith("complete"):

        try:
            todos = get_todos("todos.txt")

            index = int(user_action[9:]) -1

            completed_todo = todos[index].strip("\n")
            todos.pop(index)

            write_todos(f"todos.txt",todos)

            print(f"{completed_todo} is Completed!")

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