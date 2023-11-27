todos = []

while True:
    user_action = input("Type add, show, or quit: ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "quit":
            break
print("Bye!")