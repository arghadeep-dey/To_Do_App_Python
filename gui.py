#Importing Functions
import functions
import FreeSimpleGUI as gui

#UI Window for To Do App
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter a to-do",key="todo")
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
list_box = gui.Listbox(values = functions.get_todos(), key = 'todos',
                       enable_events=True, size=[45,10])

window = gui.Window("my to Do App",
                   layout=[[label],
                           [input_box,add_button],
                           [list_box,edit_button]],
                   font=('Helvetica', 20))
while True:
    event, values =window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            inex = todos.index(todo_to_edit)
            todos[inex] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case 'todos':
            window['todos'].update(values = values['todos'][0])

        case gui.WIN_CLOSED:
            break

window.close()

