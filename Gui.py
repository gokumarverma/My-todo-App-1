import PySimpleGUI as Sg

label_clock = Sg.Text('', key='cloack')
label_text = Sg.Text('Enter your Todo item: ', key='text')
label_input = Sg.InputText(tooltip='Enter your item', key='item')
add_button = Sg.Button('Add', key='add')
label_list = Sg.Listbox(values='', key='list_items', size=(45, 10))
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
    event, value = window.read()
    print(event, value)
window.close()
