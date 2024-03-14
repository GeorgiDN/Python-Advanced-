def math_operations(*args, **kwargs):
    for idx in range(len(args)):
        current_number = args[idx]
        if idx % 4 == 0:
            kwargs["a"] += current_number
        elif idx % 4 == 1:
            kwargs["s"] -= current_number
        elif idx % 4 == 2:
            if current_number != 0:
                kwargs["d"] /= current_number
        elif idx % 4 == 3:
            kwargs["m"] *= current_number

    sorted_values = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    formatted_values = {key: f'{value:.1f}' for key, value in sorted_values.items()}

    return "\n".join([f"{key}: {val}" for key, val in formatted_values.items()])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))




# def math_operations(*args, **kwargs):
#     operations = ""
#     steps = 0
#     for number in args:
#         steps += 1
#         if steps == 1:
#             kwargs["a"] += number
#         elif steps == 2:
#             kwargs["s"] -= number
#         elif steps == 3:
#             if number != 0:
#                 kwargs["d"] /= number
#         elif steps == 4:
#             kwargs["m"] *= number
#             steps = 0

#     sorted_data = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#     for key, value in sorted_data:
#         operations += f"{key}: {value:.1f}" + "\n"

#     return operations
  
