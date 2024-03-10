def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese_name, quantity in sorted_data:
        result.append(cheese_name)
        result.extend(sorted(quantity, reverse=True))

    return '\n'.join([str(el) for el in result])



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)



# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )




# def sorting_cheeses(**kwargs):
#     cheese_data = {}

#     for key, value in kwargs.items():
#         cheese_data[key] = value

#     sorted_cheese_data = dict(sorted(cheese_data.items(), key=lambda x: (-len(x[1]), x[0])))
#     result = ''

#     for cheese, data in sorted_cheese_data.items():
#         sorted_data = list(sorted(data, reverse=True))
#         result += f"{cheese}\n"
#         for qty in sorted_data:
#             result += f"{qty}\n"

#     return result
    
