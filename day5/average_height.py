#we want to calculate the average of any number of student heights given

student_heights = input("Input a list of student heights. ").split( , )
# result = 0
for n in range(0, len(student_heights)):
    
    student_heights[n] = int(student_heights[n])
    # result += student_heights[n]
    # average = result / len(student_heights)


total_height = 0
for height in student_heights:
    total_height += height
# print(total_height)

number_of_student = 0
for student in student_heights:
    number_of_student += 1
average_height = total_height // number_of_student
print(average_height)