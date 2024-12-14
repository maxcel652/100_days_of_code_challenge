result = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    result += student_heights[n]
    average = result / len(student_heights)