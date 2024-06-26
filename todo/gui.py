import FreeSimpleGUI
import function
import time
import os

if not os.path.exists("file.txt"):
     with open("file.txt","w") as file:
          pass

clock = FreeSimpleGUI.Text(time.strftime('%b %d, %Y %H:%M'),key='clock')
label = FreeSimpleGUI.Text("Type in a to-do")
inputbox = FreeSimpleGUI.InputText(tooltip="Enter todo",key="todo")
addbutton = FreeSimpleGUI.Button("Add")
editbutton = FreeSimpleGUI.Button("Edit")
completedbutton = FreeSimpleGUI.Button("Complete")
listbox = FreeSimpleGUI.Listbox(values=function.gettodo("file.txt"), key = "todos", enable_events= True, size = [40,10])

window = FreeSimpleGUI.Window('My To-do App', 
                              layout = [[clock],
                                        [label],
                                        [inputbox, addbutton],
                                        [listbox,editbutton,completedbutton]],
                              font=('Helvetica',15))

while True:
    event,values = window.read(timeout=1000)
    #window['clock'].update(value = time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case "Add":
            todos = function.gettodo()
            todos.append( values['todo'] + "\n" )
            function.writetodo(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todoedit = values['todos'][0]
                newtodo = values['todo'] + "\n"
                todos = function.gettodo()
                index = todos.index(todoedit)
                todos[index] = newtodo
                function.writetodo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                    FreeSimpleGUI.popup("Please select an item first.",font=('Helvetica',15))
        case "Complete":
            try:
                todocomplete = values['todos'][0]
                todos = function.gettodo()
                todos.remove(todocomplete)
                function.writetodo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                    FreeSimpleGUI.popup("Please select an item first.",font=('Helvetica',15))
        case "todos":
              window['todo'].update(value = values['todos'][0])
        case FreeSimpleGUI.WIN_CLOSED:
            break
window.close()