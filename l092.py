file = open("names.txt", "w")
try:
    file.write("Hello\n")
    file.write("This is a file")
finally:
    file.close()

# file = open("names.txt", "w")
# try:
#     print("Hello", file=file)
#     print("This is a file", file=file)
# finally:
#     file.close()
