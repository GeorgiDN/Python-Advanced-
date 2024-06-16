def softuni_students(*args, **kwargs):
    valid_courses = {}
    valid_students = {}
    not_valid_students = []

    for _id, course in kwargs.items():
        valid_courses[_id] = course

    for data in args:
        course_id = data[0]
        username = data[1]
        if course_id in valid_courses:
            valid_students[username] = valid_courses[course_id]
        else:
            not_valid_students.append(username)

    if not_valid_students:
        sorted_not_valid_students = sorted(not_valid_students)
    sorted_valid_students = dict(sorted(valid_students.items()))

    result = ''
    for username, course in sorted_valid_students.items():
        result += f"*** A student with the username {username} has successfully finished the course {course}!\n"

    if not_valid_students:
        result += f"!!! Invalid course students: {', '.join(sorted_not_valid_students)}"

    return result


# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))



# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))



# print(softuni_students(
#     ('id_22', 'Programmingkitten'),
#     ('id_11', 'MitkoTheDark'),
#     ('id_321', 'Bobosa253'),
#     ('id_08', 'KrasimirAtanasov'),
#     ('id_32', 'DaniBG'),
#     id_321='HTML & CSS',
#     id_22='Machine Learning',
#     id_08='JS Advanced',
# ))
