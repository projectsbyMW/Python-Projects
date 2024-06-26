import streamlit as sl
import function as f

def addtodo():
    todo = sl.session_state["newtodo"] + "\n"
    todos.append(todo)
    f.writetodo(todos)


todos = f.gettodo()

sl.title("My To-Do App")
sl.subheader("Give your brain a break - Note it down")
sl.write("Increase your productivity with this simple solution.")

for n, todo in enumerate(todos):
    checks = sl.checkbox(todo, key = todo)
    if checks == True:
        todos.pop(n)
        f.writetodo(todos)
        del sl.session_state[todo]
        sl.rerun()

sl.text_input(label="Enter a todo: ", 
              placeholder="Add new to-do...",
              on_change=addtodo,
              key = "newtodo")