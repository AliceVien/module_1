grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

from statistics import mean

grade_0 = mean(grades[0])
grade_1 = mean(grades[1])
grade_2 = mean(grades[2])
grade_3 = mean(grades[3])
grade_4 = mean(grades[4])

average_grades = [grade_0, grade_1, grade_2, grade_3, grade_4]

students_alphabetically = sorted(students)

student_grades = dict(zip(students_alphabetically, average_grades)) #zip создаст пары, а dict сделает словарь

print(student_grades)