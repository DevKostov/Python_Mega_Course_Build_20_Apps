# 01. Add unknown commands case_: 18

todos = []

while True:
    user_action = input("Type add, show, or quit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "quit":
            break
        case _:
            print("Hey, you entered an unknown command!")
print("Bye!")

# 02. Add Bitwise OR operator "|" 33
# todos = []
#
# while True:
#     user_action = input("Type add, show, or quit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show' | 'display':
#             for item in todos:
#                 print(item)
#         case "quit":
#             break
#         case _:
#             print("Hey, you entered an unknown command!")
# print("Bye!")

# 03. Convert the first uppercase! line 56
#
# todos = []
#
# while True:
#     user_action = input("Type add, show, or quit: ")
#     user_action = user_action.strip()
#
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case'show':
#             for item in todos:
#                 item = item.title()
#                 print(item)
#             for item in todos:
#                 print(item)
#         case "quit":
#             break
#         case _:
#             print("Hey, you entered an unknown command!")