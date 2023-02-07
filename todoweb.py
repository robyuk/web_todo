import streamlit as st
from os import path
from todofunctions import getTodoList, write_todos

_debug_ = False
TODO_FILE = "todos.txt"
NEW_TODO_PROMPT = "Enter a new todo"
NL = '\n'

if path.exists(TODO_FILE):
    todoList = getTodoList(display=_debug_)
else:
    todoList = [TODO_FILE]
    write_todos(todoList)


def add_todo():
    new_todo = st.session_state['new_todo'].strip().capitalize()

    if _debug_:
        print(new_todo)
        print(st.session_state)

    if new_todo == '' or new_todo == ' ':
        return
    
    todoList.append(new_todo + NL)
    write_todos(todoList)


def complete_todo(key):
    num = int(key)
    if _debug_:
        print("Remove", todoList[num])
    st.write(f'Completed: {todoList.pop(num)}')  # Pop the item checked
    write_todos(todoList)


# Gui.theme


if "visibility" not in st.session_state:
    st.session_state.visibility = "hidden"
    st.session_state.disabled = False
    st.session_state.placeholder = NEW_TODO_PROMPT

st.title("My Todo List")
st.subheader("A simple Todo list app")
st.write("A simple app to increase productivity")

#  st.checkbox("Label of the checkbox")

for index, todo in enumerate(todoList[1:], start=1):
    st.checkbox(todo, key=index, on_change=complete_todo, args=(str(index)),
                help="Check the box to complete this to-do")

text_input = st.text_input("newTodo",
                           label_visibility=st.session_state.visibility,
                           placeholder=st.session_state.placeholder,
                           disabled=st.session_state.disabled,
                           on_change=add_todo, key='new_todo',
                           help="Type a new to-do and press Enter to add it to the list")

if _debug_:
    if text_input:
        st.write("In the new todo box, you entered: ", text_input)
    st.write("session_state:")
    st.write(st.session_state)
    print(text_input)
    print('End.')
