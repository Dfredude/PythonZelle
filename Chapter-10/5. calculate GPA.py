from Best_GPA_detector import Student

credits, qpoints  = input('''Enter credits and quality points achieved
separated by a comma: ''').split(',')

student = Student('Fred', credits, qpoints)

print('You got a GPA of: {0:0.2f}'.format(student.gpa()))