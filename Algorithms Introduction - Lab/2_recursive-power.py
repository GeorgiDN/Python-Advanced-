def recursive_factorial(n):
    if n == 1:
        return n

    return n * recursive_factorial(n-1)


num = int(input())
print(recursive_factorial(num))



# from functools import reduce
# num = int(input())
# my_list = list(range(1, num + 1))
# res = reduce(lambda x, y: x*y, my_list)
# print(res)



# EASY WAY
# num = int(input())
# res = 1
#
# for n in range(num, 0, -1):
#     res *= n
#
# print(res)
