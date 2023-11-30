# ranking = ['John', 'Sen', 'Lisa']
#
# person_name = input("Enter a person's name: ")
# if person_name in ranking:
#     person_rank = ranking.index(person_name) + 1
#     print(person_rank)
import items

# seconds = [1.23, 1.45, 1.02]
# current = 1.11
# seconds.append(current)

# ips = ['100.122.133.105', '100.122.133.111']
# for index in enumerate(ips):
#     user_input = int(input("Enter the index of the IP you want:"))
#     print(f"You chose {ips[user_input]}")
#     break

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(seconds[1])
print(seconds)