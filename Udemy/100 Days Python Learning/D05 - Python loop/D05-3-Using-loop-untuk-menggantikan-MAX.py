# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

print(max(student_scores)) #cheat mode 
#maksud pelajaran
max_numb = 0
for semua_nilai in student_scores: #ngeloop yang ada di dalam data student_scores dan ditaruh jadi data semua_nilai
  if semua_nilai > max_numb: #jika data yang diambil dari di semua nilai > max_numb
    max_numb = semua_nilai #maka max numb yang tadinya 0 akan digantikan oleh data yang di loop, dan repeat lagi dari line 13 sampai semua data ke loop, dan berakhir dengan max numb jadi nomor paling gede
print(f"The highest score in the class is: {max_numb}")





