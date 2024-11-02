student_marks = {'name': 'Malika', 'scores': [52, 56.5, 60]}


# answer = ((sum(scores[name])) / (len(student_marks[name])))
# answer = (round(answer, 2))
answer = (sum(student_marks['scores']) / len(student_marks['scores']))
print(round(float(answer), 2))


    l1 = list(student_marks[query_name]) 

    addition = sum(l1)

    result = addition/len(l1)

    print('%.2f'% result)

