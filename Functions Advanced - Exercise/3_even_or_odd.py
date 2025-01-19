def even_odd(*args):
    nums, kind = args[:-1], args[-1]
    return [x for x in nums if x % 2 == 0] if kind == 'even' else [x for x in nums if x % 2 != 0]


#########################################################################################################################
# def even_odd(*args):
#     nums, command = list(map(int, args[:-1])), args[-1]
#     if command == "even":
#         return [n for n in nums if n % 2 == 0]
#     return [n for n in nums if n % 2 != 0]


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))



#########################################################################################################################
# def even_odd(*args):
#     *numbers, command = args
#     result = []

#     if command == "odd":
#         [result.append(x) for x in numbers if x % 2 != 0]

#     elif command == "even":
#         [result.append(x) for x in numbers if x % 2 == 0]

#     return result

# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
