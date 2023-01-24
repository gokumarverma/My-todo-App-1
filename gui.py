import time

import PySimpleGUI as Sg
import be_code

try:
    with open('Todo.txt', 'r') as file:
        file.readlines()
except FileNotFoundError:
    with open('Todo.txt', 'w') as file:
        pass


label_clock = Sg.Text('', key='clock')
label_text = Sg.Text('Enter your Todo item: ', key='text')
label_input = Sg.InputText(tooltip='Enter your item', key='item')
add_button = Sg.Button('Add', key='add')
label_list = Sg.Listbox(values=be_code.get_list(), key='list_items', enable_events=True, size=(45, 10))
edit_button = Sg.Button('Edit', key='edit')
complete_button = Sg.Button('complete', key='complete')
exit_button = Sg.Button('exit', key='exit')

layout = [[label_clock],
          [label_text],
          [label_input, add_button],
          [label_list, edit_button, complete_button],
          [exit_button]]

window = Sg.Window('My Todo App', layout=layout, font=('Helvetica', 15))

while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%Y-%m-%d %H:%M:%S'))
    match event:
        case 'add':
            todo = be_code.get_list()
            new_item = value['item']+'\n'
            if new_item in todo:
                Sg.popup("Item already in the list")
                window['item'].update(value='')
            elif '\n' == new_item:
                Sg.popup("Please enter a valid item")
                window['item'].update(value='')
            else:
                todo.append(new_item)
                be_code.write_list(todo)
                window['item'].update(value='')
                window['list_items'].update(values=be_code.get_list())
        case 'edit':
            todo = be_code.get_list()
            if not todo:
                Sg.popup("No item to edit, Please add items")
            else:
                try:
                    to_edit = value['list_items'][0]
                    index = todo.index(to_edit)
                    if value['item'] != '':
                        todo[index] = value['item']+'\n'
                        be_code.write_list(todo)
                        window['item'].update(value='')
                        window['list_items'].update(values=be_code.get_list())
                    else:
                        Sg.popup("Please provide edit value")
                except IndexError:
                    Sg.popup('Please select an item first')
        case 'complete':
            todo = be_code.get_list()
            if not todo:
                Sg.popup("No item to Complete, Please add items")
            else:
                try:
                    to_complete = value['list_items'][0]
                    print(to_complete)
                    todo = be_code.get_list()
                    print(todo)
                    todo.remove(to_complete)
                    be_code.write_list(todo)
                    window['list_items'].update(values=be_code.get_list())
                except IndexError:
                    Sg.popup('Please select an item first')
        case 'exit':
            break
        case Sg.WINDOW_CLOSED:
            break
window.close()
