def gather_credits(credits_goal, *courses_data):
    courses_info = {}
    result = []
    current_credits = 0

    for course, credits_ in courses_data:
        if current_credits < credits_goal:
            if course not in courses_info:
                courses_info[course] = credits_
                current_credits += credits_
        else:
            break

    if current_credits >= credits_goal:
        result.append(f"Enrollment finished! Maximum credits: {current_credits}.")

        result.append("Courses: " + ', '.join(sorted(courses_info.keys())))
    else:
        diff = credits_goal - current_credits
        result.append(f"You need to enroll in more courses! You have to gather {diff} credits more.")

    return '\n'.join(result)


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
