todos = []
while True:
    user_action = input("Type assign, show, edit, complete or exit: ")
    user_action = user_action.lower().strip()

    match user_action:

        case "add" | "input"| "assign":

            todo = input("Enter a todo: ") + "\n"

            with open(f"todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)


        case "show" | "display":

            with open(f"todos.txt", "r") as file:
                todos = file.readlines()

            for index,item in enumerate(todos):
                print(f"{index+1}-{item.strip("\n")}")


        case "edit" | "change" | "update":

            index = int(input("Enter the index of the todo to edit: "))
            index -= 1

            with open(f"todos.txt", "r") as file:
                todos = file.readlines()

            todo_to_change = todos[index]

            new_todo = input("Enter new todo:")
            todos[index] = new_todo + "\n"

            with open(f"todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {todo_to_change.strip("\n")} has been changed to {new_todo}")


        case "complete"| "finish":
            with open(f"todos.txt", "r") as file:
                todos = file.readlines()

            index = int(input("Position of the todo to complete: ")) -1
            todos.pop(index)

            with open(f"todos.txt", "w") as file:
                file.writelines(todos)


        case "exit" | "quit"| "bye":
            break


        case _:
            print("Invalid input")
            continue

print ("Goodbye")