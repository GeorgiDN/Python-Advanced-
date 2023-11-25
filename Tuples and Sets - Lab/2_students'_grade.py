number_students = int(input())
grades = {}

for _ in range(number_students):
    info = input().split(' ')
    name = info[0]
    grade = float(info[1])

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name, grade_list in grades.items():
    average_grade = sum(grade_list) / len(grade_list)
    formatted_grades = ' '.join([f'{grade:.2f}' for grade in grade_list])
    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
