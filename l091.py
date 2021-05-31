file = open("cities.txt", "r")
try:
    for line in file:
        print(line.strip())
finally:
    file.close()
