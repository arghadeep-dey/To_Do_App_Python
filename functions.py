# Functions for File Management
def get_todos(filepath="todos.txt"):
    """Return a list of all todos from the parameter file"""
    with open(filepath, "r") as file_local:
        local_todos = file_local.readlines()
    return local_todos

def write_todos(todos_arg,filepath="todos.txt"):
    """Edit the todos file with the parameter file"""
    try:
        with open(filepath, "w") as file_local:
            file_local.writelines(todos_arg)
        return 1
    except FileNotFoundError:
        print(f"{filepath} does not exist")
        return 0
