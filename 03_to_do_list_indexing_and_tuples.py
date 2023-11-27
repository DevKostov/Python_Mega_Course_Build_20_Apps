todos = []

while True:
    user_action = input("Type add, show, edit or quit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter the number of the todo you want to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case "quit":
            break
print("Bye!")