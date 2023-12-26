def word_length(word):
    return len(word)


def create_a_model(words):
    return ", ".join([f"{n} -> {word_length(n)}" for n in words])


def print_result(res):
    return print(res)


def take_input():
    return input().split(", ")


print_result(create_a_model(take_input()))


# One row
#print(", ".join([f"{n} -> {len(n)}" for n in input().split(", ")]))
