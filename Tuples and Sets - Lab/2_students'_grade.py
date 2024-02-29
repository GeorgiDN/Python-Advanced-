number_of_students = int(input())
students_records = {}

for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)

    if name not in students_records:
        students_records[name] = []
    students_records[name].append(grade)

for curr_name, marks in students_records.items():
    average_grade = sum(marks) / len(marks)
    formatted_grades = [f"{mark:.2f}" for mark in marks]
    print(f"{curr_name} -> {' '.join(map(str, formatted_grades))} (avg: {average_grade:.2f})")



# number_of_students = int(input())
# students_records = {}

# for _ in range(number_of_students):
#     name, assessment = input().split()
#     assessment = float(assessment)

#     if name not in students_records:
#         students_records[name] = []
#     students_records[name].append(assessment)

# for curr_name, marks in students_records.items():
#     average_grade = sum(marks) / len(marks)
#     formatted_assessments = []
#     for mark in marks:
#         formatted_assessments.append(f"{mark:.2f}")
#     print(f"{curr_name} -> {' '.join(map(str, formatted_assessments))} (avg: {average_grade:.2f})")




# number_students = int(input())
# grades = {}

# for _ in range(number_students):
#     info = input().split(' ')
#     name = info[0]
#     grade = float(info[1])

#     if name not in grades:
#         grades[name] = []
#     grades[name].append(grade)

# for name, grade_list in grades.items():
#     average_grade = sum(grade_list) / len(grade_list)
#     formatted_grades = ' '.join([f'{grade:.2f}' for grade in grade_list])
#     print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
