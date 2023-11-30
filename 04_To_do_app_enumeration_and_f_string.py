todos = []

while True:
    user_action = input("Type add, show, complete or quit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of the todo you want to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number of the todo you want to complete: "))
            todos.pop(number - 1)
        case "quit":
            break
print("Bye!")