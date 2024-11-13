# Given the names and grades for each student in a class of  students, 
#     store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, 
#     order their names alphabetically and print each name on a new line.

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

grades = []
for x in students:
    grades.append(x[1])

second_lowest = (sorted(list(set(grades)))[1])

second_lowest_list = []

for x in students:
    if x[1] == second_lowest:
        second_lowest_list.append(x[0])

second_lowest_list = (sorted(second_lowest_list))

for x in second_lowest_list:
    print(x)