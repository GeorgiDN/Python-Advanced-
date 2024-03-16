file_name = "my_first_file.txt"

with open(file_name, "w") as file:
    file.write('I just created my first file!')




# different ways
# file = open("my_first_file.txt", "a")
# file.write("This is my first line.\n")
# more_information = ["Multiple line\n",
#                     "Adding the lines to a list\n",
#                     "But we have to use '.writelines()'\n"]
# file.writelines(more_information)
# file.close()




# with open("my_first_file.txt", "w") as f:
#     f.write('This is my first line.\n')
#     more_info = ["Multiple line\n",
#                  "Add line to a list\n"
#                  "And we use .writelines()\n"]
#     f.writelines(more_info)
