# https://judge.softuni.org/Contests/Practice/Index/1832#0

from collections import Counter

list_numbers = [float(x) for x in input().split()]
occurrences = Counter(list_numbers)
print("\n".join([f"{x} - {y} times" for x, y in occurrences.items()]))


#############################################################################
# from collections import Counter
# print("\n".join([f"{x} - {y} times" for x, y in Counter([float(n) for n in input().split()]).items()]))



#############################################################################
# from collections import Counter
# list_numbers = [float(x) for x in input().split()]
# print("\n".join([f"{x} - {y} times" for x, y in Counter(list_numbers).items()]))



#############################################################################
# list_numbers = [float(x) for x in input().split()]
# occurrences = {}
#
# for num in list_numbers:
#     if num not in occurrences:
#         occurrences[num] = 0
#     occurrences[num] += 1
#
# print("\n".join([f"{x} - {y} times" for x, y in occurrences.items()]))



#############################################################################
# numbers = list(map(float, input().split(" ")))
# numbers_counter = {}
#
# for num in numbers:
#     if num not in numbers_counter:
#         numbers_counter[num] = 1
#     else:
#         numbers_counter[num] += 1
#
# for key, value in numbers_counter.items():
#     print(f"{key} - {value} times")
