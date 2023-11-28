FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as r_file:
        local_todos = r_file.readlines()
    return local_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as w_file:
        w_file.writelines(todos_arg)


# show todos list only when run functions.py
# otherwise it prints Welcome.
if __name__ == "__main__":
    print(get_todos())
else:
    print('\n' + "Welcome to my todos app!")
