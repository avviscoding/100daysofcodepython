student_scores = input("input a list of students grades")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    print(student_scores)


highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"my highest score is {highest_score}")


