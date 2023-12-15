def age_assignment(*args, **kwargs):
    result = {}
    names = []

    for key, val in kwargs.items():
        result[key] = val

    for name in args:
        names.append(name)
        if name[0] in result.keys():
            result[name] = result[name[0]]
            del result[name[0]]

    result_sorted = dict(sorted(result.items()))

    #####  3 lines
    # final_result = ''
    # for k, v in result_sorted.items():
    #     final_result += f"{k} is {v} years old.\n"

    #####  1 line
    final_result = '\n'.join([f"{k} is {v} years old." for k, v in result_sorted.items()])

    return final_result

print(age_assignment("Bill", "Amy", "Willy", W=36, A=22, B=61))
