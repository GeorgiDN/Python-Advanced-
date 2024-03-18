from fibonacci_module.fibonacci_sequence_functions import locate_number, create_sequence


def fibonacci_sequence():
    while True:
        command = input()

        if command.startswith('Stop'):
            break
        elif command.startswith('Create'):
            print(create_sequence(int(command.split()[2])))
        elif command.startswith('Locate'):
            print(locate_number(int(command.split()[1])))


fibonacci_sequence()
