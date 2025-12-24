todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.lower().strip()
    match user_action:
        case "add" | "input":
            todo = input("Enter a todo: ")
            todos.append(todo.strip())
        case "show" | "display":
            for item in todos:
                print(item)
        case "edit" | "change" | "update":
            index = int(input("Enter the index of the todo to edit: "))
            index -= 1
            new_todo = input("Enter new todo:")
            todos[index] = new_todo
        case "exit" | "quit":
            break
        case _:
            print("Invalid input")
            continue

print ("Goodbye")