def concatenate(*args, **kwargs):
    string_concatenation = "".join(args)

    for key in kwargs:
        if key in string_concatenation:
            string_concatenation = string_concatenation.replace(key, kwargs[key])

    return string_concatenation

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
