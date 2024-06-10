def gather_credits(*args):
    credits_goal = int(args[0])
    rest = args[1:]
    result = ''

    gathered_credits = 0
    enrolled_courses = []

    for course, _credits in rest:
        if gathered_credits >= credits_goal:
            break
        if course not in enrolled_courses:
            enrolled_courses.append(course)
            gathered_credits += _credits

    if gathered_credits >= credits_goal:
        result += f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
        sorted_enrolled_courses = sorted(enrolled_courses)
        all_courses = ", ".join(sorted_enrolled_courses)
        result += f"Courses: {all_courses}"
    else:
        credits_shortage = credits_goal - gathered_credits
        result += f"You need to enroll in more courses! You have to gather {credits_shortage} credits more.\n"

    return result



# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))


# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))


# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))








# def gather_credits(credits_goal, *courses_data):
#     courses_info = {}
#     result = []
#     current_credits = 0
# 
#     for course, credits_ in courses_data:
#         if current_credits < credits_goal:
#             if course not in courses_info:
#                 courses_info[course] = credits_
#                 current_credits += credits_
#         else:
#             break
# 
#     if current_credits >= credits_goal:
#         result.append(f"Enrollment finished! Maximum credits: {current_credits}.")
# 
#         result.append("Courses: " + ', '.join(sorted(courses_info.keys())))
#     else:
#         diff = credits_goal - current_credits
#         result.append(f"You need to enroll in more courses! You have to gather {diff} credits more.")
# 
#     return '\n'.join(result)
# 
# 
# # print(gather_credits(
# #     60,
# #     ("Basics", 27),
# #     ("Fundamentals", 27),
# #     ("Advanced", 30),
# #     ("Web", 30)
# # ))
# 
