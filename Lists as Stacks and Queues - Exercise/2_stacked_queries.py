PUSH = "1"
DELETE = "2"
PRINT_MAX = "3"
PRINT_MIN = "4"


def push_the_number(stack_, current_number_):
    stack_.append(current_number_)
    return stack_


def delete(stack_):
    if stack_:
        stack_.pop()
    return stack_


def print_max(stack_):
    if stack_:
        return print(max(stack_))


def print_min(stack_):
    if stack_:
        return print(min(stack_))


def main():
    stack = []
    count = int(input())
    for _ in range(count):
        data = input().split()
        if data[0] == PUSH:
            current_number = int(data[1])
            stack = push_the_number(stack, current_number)

        elif data[0] == DELETE:
            stack = delete(stack)

        elif data[0] == PRINT_MAX:
            print_max(stack)

        elif data[0] == PRINT_MIN:
            print_min(stack)

    if stack:
        numbers_in_reversed = stack[::-1]
        print(", ".join(map(str, numbers_in_reversed)))


if __name__ == '__main__':
    main()




# PUSH = "1"
# DELETE = "2"
# PRINT_MAX = "3"
# PRINT_MIN = "4"


# def push(num, stack):
#     stack.append(num)
#     return stack


# def delete(stack):
#     stack.pop()
#     return stack


# def print_max(stack):
#     max_num = max([int(el) for el in stack])
#     return max_num


# def print_min(stack):
#     min_num = min([int(el) for el in stack])
#     return min_num


# def main(queries):
#     nums = []
#     result = []
#     for _ in range(queries):
#         command = input()
#         if command.startswith(PUSH):
#             query = command.split(" ")
#             nums = push(query[1], nums)
#         elif command == DELETE and nums:
#             nums = delete(nums)
#         elif command == PRINT_MAX and nums:
#             print(print_max(nums))
#         elif command == PRINT_MIN and nums:
#             print(print_min(nums))

#     while nums:
#         result.append(nums.pop())

#     print(f"{', '.join(result)}")


# main(int(input()))
