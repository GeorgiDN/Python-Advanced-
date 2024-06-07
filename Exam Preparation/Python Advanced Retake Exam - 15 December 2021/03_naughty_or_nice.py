def check_length_and_fill_list(matched_kids, action, nice_list, naughty_list, santa_list):
    if len(matched_kids) == 1:
        kid = matched_kids[0]
        if action == "Nice":
            nice_list.append(kid[1])
        elif action == "Naughty":
            naughty_list.append(kid[1])
        santa_list.remove(kid)

    return nice_list, naughty_list, santa_list


def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_list = []
    naughty_list = []

    for command in args:
        count, kind = command.split('-')
        count = int(count)

        matched_kids = [kid for kid in santa_list if kid[0] == count]

        nice_list, naughty_list, santa_list = (
            check_length_and_fill_list(matched_kids, kind, nice_list, naughty_list, santa_list))

    for name, kind in kwargs.items():
        matched_kids = [kid for kid in santa_list if kid[1] == name]

        nice_list, naughty_list, santa_list = (
            check_length_and_fill_list(matched_kids, kind, nice_list, naughty_list, santa_list))

    not_found_list = [kid[1] for kid in santa_list]

    result = []
    if nice_list:
        result.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        result.append(f"Naughty: {', '.join(naughty_list)}")
    if not_found_list:
        result.append(f"Not found: {', '.join(not_found_list)}")

    return "\n".join(result)


# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))


# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

