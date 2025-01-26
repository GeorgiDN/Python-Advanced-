import os


def create_file(file_name):
    with open(file_name, 'w') as f:
        pass


def add_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(f"{content}\n")


def replace_string(file_name, old_string, new_string):
    try:
        with open(file_name, "r+") as file:
            text = file.read()
            text = text.replace(old_string, new_string)

            file.seek(0)
            file.write(text)
            file.truncate()

    except FileNotFoundError:
        print(f"An error occurred!")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print(f"An error occurred!")


while True:
    command_info = input()
    if command_info == 'End':
        break

    command, file_name = command_info.split('-')[0], command_info.split('-')[1]

    if command == 'Create':
        create_file(file_name)

    elif command == 'Add':
        content = command_info.split('-')[2]
        add_file(file_name, content)

    elif command == 'Replace':
        old_string, new_string = command_info.split('-')[2], command_info.split('-')[3]
        replace_string(file_name, old_string, new_string)

    elif command == 'Delete':
        delete_file(file_name)



###############################################################################################################################################
# import os


# def create_file(current_file):
#     with open(current_file, "w") as file:
#         pass
#     return current_file


# def add_file(current_file, curr_content):
#     with open(current_file, "a") as file:
#         file.write(curr_content + '\n')
#     return current_file


# def replace_content(current_file, old_str, new_str):
#     try:
#         with open(current_file, 'r') as file:
#             text = file.read()

#         text = text.replace(old_str, new_str)

#         with open(current_file, "w") as output_file:
#             output_file.write(text)

#         return current_file

#     except FileNotFoundError:
#         return print("An error occurred")


# def delete_file(current_file):
#     try:
#         os.remove(current_file)

#     except FileNotFoundError:
#         print("An error occurred")


# while True:
#     command = input()
#     if command == "End":
#         break

#     data = command.split('-')
#     current_command = data[0]

#     if current_command == "Create":
#         file_name = data[1]
#         create_file(file_name)

#     elif current_command == "Add":
#         file_name, content = data[1], data[2]
#         add_file(file_name, content)

#     elif current_command == "Replace":
#         file_name, old_string, new_string = data[1], data[2], data[3]
#         replace_content(file_name, old_string, new_string)

#     elif current_command == "Delete":
#         file_name = data[1]
#         delete_file(file_name)




# TEST CODES
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# End
