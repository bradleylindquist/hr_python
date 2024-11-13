# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# dict = hash 

student1_marks = {'name': 'Malika', 'scores': [52, 56.5, 60]}
student2_marks = {'name': 'Krishna', 'scores': [67, 68, 69]}
student3_marks = {'name': 'Arjun', 'scores': [70, 98, 63]}

answer = (sum(student2_marks['scores']) / len(student2_marks['scores']))
print(student2_marks['name'], round(float(answer), 2))



