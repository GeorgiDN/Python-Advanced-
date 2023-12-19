file_name = "text.txt"

try:
    with open(file_name, "r") as file:
        file_content = file.read()
        print("File found")

except FileNotFoundError:
    print("File not found")




# file_name = "text.txt"

# try:
#     file = open(file_name, "r")
#     print("File found")
#     file.close()
# except FileNotFoundError:
#     print("File not found")
