def even_odd_filter(**kwargs):
    my_dict = {}
    for kind, nums in kwargs.items():
        my_dict[kind] = []
        for num in nums:
            if kind == "even" and num % 2 == 0:
                my_dict["even"].append(num)
            elif kind == "odd" and num % 2 != 0:
                my_dict["odd"].append(num)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))



# def even_odd_filter(**kwargs):
#     result = {}

#     for key in kwargs:
#         if key == "odd":
#             result[key] = [x for x in kwargs[key] if x % 2 != 0]
#         elif key == "even":
#             result[key] = [x for x in kwargs[key] if x % 2 == 0]

#     return dict(sorted(result.items(), key=lambda x: -len(x[1])))



# # print(even_odd_filter(
# #     odd=[2, 2, 30, 44, 10, 5],
# # ))

# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))




#######
# def even_odd_filter(**kwargs):
#     numbers = {}

#     if "even" in kwargs:
#         match_even = list(filter(lambda x: x % 2 == 0, kwargs["even"]))
#         numbers["even"] = match_even

#     if "odd" in kwargs:
#         match_odd = list(filter(lambda x: x % 2 != 0, kwargs["odd"]))
#         numbers["odd"] = match_odd

#     return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))

# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
