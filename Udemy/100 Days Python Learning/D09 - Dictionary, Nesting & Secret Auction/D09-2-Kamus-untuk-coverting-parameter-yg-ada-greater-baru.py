student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆


student_grades = {} #format untuk kamus kosong


for student in student_scores: #looping key dari kamus
    scoring = student_scores[student] # value=kamus[key], format pemanggilan data value
    print(scoring)
    if scoring > 90:
        student_grades[student] = "Outstanding"
        #format untuk penggantian value baru
        #kamus_baru[Key] = value baru
    elif scoring >80:
        student_grades[student] = "Exceeds Expectations" ##format => kamus baru[key lama] = value baru
    elif scoring >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)





