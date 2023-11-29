#  https://judge.softuni.org/Contests/Compete/DownloadResource/41550

from _collections import deque


def is_subset(n1, n2):
    if set(n2) <= set(n1) or set(n1) <= set(n2):
        print("True")
    else:
        print('False')


first_sequence = deque(int(el) for el in input().split(" "))
second_sequence = deque(int(el) for el in input().split(" "))

n = int(input())

for _ in range(n):
    command = input()

    if command.startswith('Add First'):
        command = command.split(' ')
        for ch in command:
            if ch.isdigit():
                if int(ch) not in first_sequence:
                    first_sequence.append(int(ch))

    elif command.startswith('Add Second'):
        command = command.split(' ')
        for ch in command:
            if ch.isdigit():
                if int(ch) not in second_sequence:
                    second_sequence.append(int(ch))

    elif command.startswith('Remove First'):
        command = command.split(' ')
        for ch in command:
            if ch.isdigit():
                if int(ch) in first_sequence:
                    while int(ch) in first_sequence:
                        first_sequence.remove(int(ch))

    elif command.startswith('Remove Second'):
        command = command.split(' ')
        for ch in command:
            if ch.isdigit():
                if int(ch) in second_sequence:
                    while int(ch) in second_sequence:
                        second_sequence.remove(int(ch))

    elif command.startswith('Check'):
        is_subset(first_sequence, second_sequence)

first_sequence = set(first_sequence)
second_sequence = set(second_sequence)

first_sequence = list(sorted(first_sequence))
second_sequence = list(sorted(second_sequence))

print(', '.join(map(str, first_sequence)))
print(', '.join(map(str, second_sequence)))
