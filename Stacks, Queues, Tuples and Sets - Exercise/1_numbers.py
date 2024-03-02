from collections import deque


def clear_repeated_numbers(first_sequence_, second_sequence_):
    first_sequence_ = set(first_sequence_)
    second_sequence_ = set(second_sequence_)
    first_sequence_ = list(first_sequence_)
    second_sequence_ = list(second_sequence_)

    return first_sequence_, second_sequence_


def add(sequence, numbers_data_):
    for _ in range(len(numbers_data_)):
        num = numbers_data_.popleft()
        if num not in sequence:
            sequence.append(num)
    return sequence


def remove(sequence, numbers_data_):
    for _ in range(len(numbers_data_)):
        num = numbers_data_.popleft()
        if num in sequence:
            sequence.remove(num)
    return sequence


def is_subset(first_sequence_, second_sequence_):
    if set(second_sequence_) <= set(first_sequence_) or set(first_sequence_) <= set(second_sequence_):
        print("True")
    else:
        print('False')


def sort_the_sequence(first_sequence_, second_sequence_):
    first_sequence_ = list(sorted(first_sequence_))
    second_sequence_ = list(sorted(second_sequence_))
    return first_sequence_, second_sequence_


def print_result(first_sequence_, second_sequence_):
    result = []
    result.append(', '.join(map(str, first_sequence_)))
    result.append(', '.join(map(str, second_sequence_)))
    return print('\n'.join(map(str, result)))


def main():
    first_sequence = [int(x) for x in input().split()]
    second_sequence = [int(x) for x in input().split()]
    rows = int(input())
    first_sequence, second_sequence = clear_repeated_numbers(first_sequence, second_sequence)

    for _ in range(rows):
        data = input().split()
        command = data[0]
        info = data[1]

        if command == "Add":
            numbers_data = deque(map(int, data[2:]))
            if info == "First":
                first_sequence = add(first_sequence, numbers_data)

            elif info == "Second":
                second_sequence = add(second_sequence, numbers_data)

        elif command == "Remove":
            numbers_data = deque(map(int, data[2:]))
            if info == "First":
                first_sequence = remove(first_sequence, numbers_data)

            elif info == "Second":
                second_sequence = remove(second_sequence, numbers_data)

        elif command == "Check":
            is_subset(first_sequence, second_sequence)

    first_sequence, second_sequence = sort_the_sequence(first_sequence, second_sequence)
    print_result(first_sequence, second_sequence)


if __name__ == "__main__":
    main()




##################################################################################################
# from collections import deque
#
#
# def add(sequence, numbers_data_):
#     for _ in range(len(numbers_data_)):
#         num = numbers_data_.popleft()
#         if num not in sequence:
#             sequence.append(num)
#     return sequence
#
#
# def remove(sequence, numbers_data_):
#     for _ in range(len(numbers_data_)):
#         num = numbers_data_.popleft()
#         if num in sequence:
#             sequence.remove(num)
#     return sequence
#
#
# def check_susbset(first_sequence_, second_sequence_):
#     if set(second_sequence_) <= set(first_sequence_) or set(first_sequence_) <= set(second_sequence_):
#         print("True")
#     else:
#         print('False')
#
#
# def sort_the_sequence(first_sequence_, second_sequence_):
#     first_sequence_ = list(sorted(first_sequence_))
#     second_sequence_ = list(sorted(second_sequence_))
#     return first_sequence_, second_sequence_
#
#
# first_seq = [int(x) for x in input().split()]
# second_seq = [int(x) for x in input().split()]
#
#
# first_sequence = []
# for el in first_seq:
#     if el not in first_sequence:
#         first_sequence.append(el)
# second_sequence = []
# for el in second_seq:
#     if el not in second_sequence:
#         second_sequence.append(el)
#
#
# rows = int(input())
#
#
# for _ in range(rows):
#     data = input().split()
#     command = data[0]
#     info = data[1]
#
#     if command == "Add":
#         numbers_data = deque(map(int, data[2:]))
#         if info == "First":
#             first_sequence = add(first_sequence, numbers_data)
#
#         elif info == "Second":
#             second_sequence = add(second_sequence, numbers_data)
#
#     elif command == "Remove":
#         numbers_data = deque(map(int, data[2:]))
#         if info == "First":
#             first_sequence = remove(first_sequence, numbers_data)
#
#         elif info == "Second":
#             second_sequence = remove(second_sequence, numbers_data)
#
#     elif command == "Check":
#         check_susbset(first_sequence, second_sequence)
#
#     first_sequence, second_sequence = sort_the_sequence(first_sequence, second_sequence)
#
#
# print(', '.join(map(str, first_sequence)))
# print(', '.join(map(str, second_sequence)))




############################################################################################################
# from _collections import deque
# 
# 
# def is_subset(n1, n2):
#     if set(n2) <= set(n1) or set(n1) <= set(n2):
#         print("True")
#     else:
#         print('False')
# 
# 
# first_sequence = deque(int(el) for el in input().split(" "))
# second_sequence = deque(int(el) for el in input().split(" "))
# 
# n = int(input())
# 
# for _ in range(n):
#     command = input()
# 
#     if command.startswith('Add First'):
#         command = command.split(' ')
#         for ch in command:
#             if ch.isdigit():
#                 if int(ch) not in first_sequence:
#                     first_sequence.append(int(ch))
# 
#     elif command.startswith('Add Second'):
#         command = command.split(' ')
#         for ch in command:
#             if ch.isdigit():
#                 if int(ch) not in second_sequence:
#                     second_sequence.append(int(ch))
# 
#     elif command.startswith('Remove First'):
#         command = command.split(' ')
#         for ch in command:
#             if ch.isdigit():
#                 if int(ch) in first_sequence:
#                     while int(ch) in first_sequence:
#                         first_sequence.remove(int(ch))
# 
#     elif command.startswith('Remove Second'):
#         command = command.split(' ')
#         for ch in command:
#             if ch.isdigit():
#                 if int(ch) in second_sequence:
#                     while int(ch) in second_sequence:
#                         second_sequence.remove(int(ch))
# 
#     elif command.startswith('Check'):
#         is_subset(first_sequence, second_sequence)
# 
# first_sequence = set(first_sequence)
# second_sequence = set(second_sequence)
# 
# first_sequence = list(sorted(first_sequence))
# second_sequence = list(sorted(second_sequence))
# 
# print(', '.join(map(str, first_sequence)))
# print(', '.join(map(str, second_sequence)))

