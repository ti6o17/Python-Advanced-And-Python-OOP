grades_input = int(input())
dict_students_grades = {}
for _ in range(grades_input):
    name, grade_str = input().split()
    grade = float(grade_str)
    if name in dict_students_grades:
        dict_students_grades[name].append(grade)
    else:
        dict_students_grades[name] = []
        dict_students_grades[name].append(grade)
for data in dict_students_grades.items():
    # str_grades = ' '.join(dict_students_grades[name])
    #
    sum_grades = [float(num) for num in data[1]]
    print(f"{data[0]} -> {' '.join([f'{num:.2f}' for num in data[1]])} (avg: {(sum(data[1]) / (len(data[1]))):.2f})")
