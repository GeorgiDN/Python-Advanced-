def age_assignment(*args, **kwargs):
    person_info = {}
    for name in args:
        for letter in name:
            if letter in kwargs:
                person_info[name] = kwargs[letter]

    sorted_person_info = dict(sorted(person_info.items()))
    result = '\n'.join([f'{person} is {age} years old.' for person, age in sorted_person_info.items()])

    return result


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))




# def age_assignment(*args, **kwargs):
#     result = {}
#     names = []
# 
#     for key, val in kwargs.items():
#         result[key] = val
# 
#     for name in args:
#         names.append(name)
#         if name[0] in result.keys():
#             result[name] = result[name[0]]
#             del result[name[0]]
# 
#     result_sorted = dict(sorted(result.items()))
# 
# 
#     # final_result = ''
#     # for k, v in result_sorted.items():
#     #     final_result += f"{k} is {v} years old.\n"
# 
#     
#     final_result = '\n'.join([f"{k} is {v} years old." for k, v in result_sorted.items()])
# 
#     return final_result
# 




# def age_assignment(*args, **kwargs):
#     result = ""
# 
#     for full_name in args:
#         first_letter = full_name[0]
#         kwargs[full_name] = kwargs[first_letter]
#         del kwargs[first_letter]
# 
#     sorted_names = sorted(kwargs.items(), key=lambda x: x[0])
# 
#     for name, age in sorted_names:
#         result += f"{name} is {age} years old." + "\n"
# 
#     return result
# 
