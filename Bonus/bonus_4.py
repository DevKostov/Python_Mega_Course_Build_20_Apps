# waiting_list = ["sen", "ben", "john"]
# waiting_list.sort()
#
# for index, item in enumerate(waiting_list):
#     row = f"{index + 1}-{item.capitalize()}"
#     print(row)
import item

filenames = ['document.txt', 'report.txt', 'presentation.txt']
filenames.sort()

for index, item in enumerate(filenames):
    row = f"{index}-{item.capitalize()}"
    print(row)