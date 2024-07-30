def students_credits(*args):
    diyan_results = {}
    required_credits = 240

    for data in args:
        courses_info = data.split('-')
        course_name = courses_info[0]
        credits_, max_test_points, diyan_points = int(courses_info[1]), int(courses_info[2]), int(courses_info[3])

        numbers_of_credits = (diyan_points * credits_) / max_test_points if max_test_points > 0 else 0
        diyan_results[course_name] = numbers_of_credits

    total_earn_credits = sum(diyan_results.values())
    sorted_diyan_results = dict(sorted(diyan_results.items(), key=lambda x: x[1], reverse=True))
    result = []

    if total_earn_credits >= required_credits:
        result.append(f"Diyan gets a diploma with {total_earn_credits:.1f} credits.")
    else:
        needed_credits = required_credits - total_earn_credits
        result.append(f"Diyan needs {needed_credits:.1f} credits more for a diploma.")

    for course, cred in sorted_diyan_results.items():
        result.append(f"{course} - {cred:.1f}")

    return "\n".join(result)


# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )

# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
