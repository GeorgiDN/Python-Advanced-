def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))



# def get_info(**kwargs):
#     person_info = {}
#     for key, value in kwargs.items():
#         person_info[key] = value
# 
#     result = f"This is {person_info['name']} from {person_info['town']} and he is {person_info['age']} years old"
#     return result
# 
# 
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))



# def get_info(name, age, town):
#     return f"This is {name} from {town} and he is {age} years old"
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
