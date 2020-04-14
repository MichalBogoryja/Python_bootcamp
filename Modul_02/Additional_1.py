exam_points = {
    "Mariusz": 30,
    "Mateusz": 55,
    "Marta": 76,
    "Roman": 30,
    "Arleta": 59,
    "Adrian": 96,
    "Monika": 91,
    "Andrzej": 22,
    "Krzysztof": 83,
    "Krystyna": 93,
    "Piotr": 44,
    "Dawid": 10,
    "Agnieszka": 15
}

failed_students = []
top_students = []
best_student = ("", 0)


for student in exam_points:
    if exam_points[student] > best_student[1]:
       best_student = (student, exam_points[student])

    if exam_points[student] <= 45:
        failed_students += [student]
    elif exam_points[student] >= 91:
        top_students += [student]

print(f"Failed: {failed_students},\nTop {top_students},\nBest student: {best_student}")
