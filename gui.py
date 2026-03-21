#Importing Functions
import functions
import FreeSimpleGUI as Gui
import time

Gui.theme('DarkAmber')

#UI Window for To Do App
clock = Gui.Text('',key='clock')
label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter a to-do",key="todo")
add_button = Gui.Button("Add")
edit_button = Gui.Button("Edit")
complete_button = Gui.Button("Complete")
exit_button = Gui.Button("Exit")
list_box = Gui.Listbox(values = functions.get_todos(), key = 'todos',
                       enable_events=True, size=(45,10))

window = Gui.Window("my to Do App",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

#Functionality for the UI Window
while True:
    event, values = window.read(timeout=250)
    # Exit immediately on close so we don't try to update widgets during teardown.
    if event in (None, Gui.WIN_CLOSED, Gui.WINDOW_CLOSED, "Exit"):
        break

    values = values or {}
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # Debugging (optional):
    # print(1, event)
    # print(2, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip() + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                Gui.popup("Please Select an Item for Edit",
                          font = ('Helvetica', 20))

        case "Complete":
            try:
                todos_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window["todo"].update(value='')
            except IndexError:
                Gui.popup("Please Select an Item for Complete",
                          font = ('Helvetica', 20))

        case 'todos':
            if values.get("todos"):
                window["todo"].update(value=values["todos"][0].strip())

window.close()
