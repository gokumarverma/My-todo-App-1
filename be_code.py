def get_list(filepath='Todo.txt'):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data


def write_list(items, filepath='Todo.txt'):
    with open(filepath, 'w') as file:
        file.writelines(items)
