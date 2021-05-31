import json

file = open("employee.json", "r")
try:
    file_content = file.read()
    data = json.loads(file_content)
    print(data)
finally:
    file.close()
