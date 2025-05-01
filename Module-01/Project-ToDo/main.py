todos = []

while True:
    user_option = input(
        "Choose your option: Add / List / Edit / Exit: ").strip().upper()

    match user_option:
        case 'ADD':
            todo = input("Enter your task: ").strip().title()
            todos.append(todo)
            print("Task Added.")
        case 'LIST':
            for index, item in enumerate(todos, start=1):
                print(index, item, sep='->')
        case 'EDIT':
            print('Edited')
        case 'EXIT':
            break
        case _:
            print("Invalid Option.")
print("System Closed...")
