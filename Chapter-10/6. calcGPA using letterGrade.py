from Best_GPA_detector import Student

credits, letterGrade  = input('''Enter credits and letter grade achieved
separated by a comma: ''').split(',')
print(type(credits), type(letterGrade))
student = Student('Fred', 0, 0)
student.addLetterGrade(letterGrade, credits)
print(student.getHours(), student.getQPoints())
print('You got a GPA of: {0:0.2f}'.format(student.gpa()))