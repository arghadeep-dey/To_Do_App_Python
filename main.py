todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        with open(f"todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)


    elif user_action.startswith("show"):

        with open(f"todos.txt", "r") as file:
            todos = file.readlines()

        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip("\n")}")


    elif user_action.startswith("edit"):

        try:
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

        except ValueError:
            print("Invalid command! Syntax for Edit Command is edit <index of list to be changed>")
            continue
        except IndexError:
            print("Invalid Index Number! Please enter a valid index")
            continue

    elif user_action.startswith("complete"):

        try:
            with open(f"todos.txt", "r") as file:
                todos = file.readlines()

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