import csv

# file = open("staff.csv", "r")
# try:
#     csv_reader = csv.reader(file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print("Column names are ", row)
#         else:
#             print("Name:", row[0], "Department:", row[1], "Age:", row[2])
#         line_count += 1
# finally:
#     file.close()

import csv

file = open("staff.csv", "r")
try:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print("Name:", row["name"],
              "Department:", row["department"],
              "Age:", row["age"])
finally:
    file.close()
