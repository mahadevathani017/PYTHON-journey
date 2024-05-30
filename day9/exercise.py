student_scores={
    "Harry":81,
    "Ron":78,
    "Harmione":99,
    "Draco":74,
    "Nevillie":62
}

student_grades={}#empty dictionary

for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="S"
    elif score>80:
        student_grades[student]="A"
    elif score>70:
        student_grades[student]="B"
    else:
        student_grades[student]="C"
print(student_grades)
