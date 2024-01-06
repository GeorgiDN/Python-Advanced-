def softuni_students(*args, **kwargs):
    valid_courses = {}
    valid_students = {}
    not_valid_students = []

    for key, val in kwargs.items():
        valid_courses[key] = val

    for info in args:
        id_ = info[0]
        name = info[1]
        if id_ in valid_courses:
            valid_students[name] = valid_courses[id_]
        else:
            not_valid_students.append(name)

    if not_valid_students:
        sorted_not_valid_students = sorted(not_valid_students)
    sorted_valid_students = dict(sorted(valid_students.items()))

    final_result = ''
    for k, v in sorted_valid_students.items():
        final_result += f"*** A student with the username {k} has successfully finished the course {v}!\n"

    if not_valid_students:
        final_result += f"!!! Invalid course students: {', '.join(sorted_not_valid_students)}"

    return final_result


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
