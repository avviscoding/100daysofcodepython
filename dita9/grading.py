student_scores = {
    "harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
# line 8 empty dictionairy
for student in student_scores:
 score = student_scores[student]
 if score > 90:
    student_grades[student] = "Outstanding"
 elif score > 80:
     student_grades[student] = "Exxceds expectetions"
 elif score > 70:
     student_grades[student] = "Acceptable"
 else:
     student_grades[student] = "Fail :/"


print(student_grades)