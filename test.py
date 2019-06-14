import os
file = open('calendar.txt', "r")
file_content = file.read()
calendar = {}
if os.path.exists('calendar.txt') == False:
    file = open('calendar.txt', "a").close()
    file_content = file.read()
print(file_content)


