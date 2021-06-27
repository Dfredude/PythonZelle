#gpa.py
#Finds student highest GPA

class Student:
    def __init__(self, name, hours, qpoints) -> None:
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        self.hours += credits
        self.qpoints += gradePoint
    
    def addLetterGrade(self, gradeLetter, credits):
        wrong_input = False
        if gradeLetter == 'A': grade = 4
        elif gradeLetter == 'B': grade = 3
        elif gradeLetter == 'C': grade = 2
        elif gradeLetter == 'D': grade = 1
        elif gradeLetter == 'F': grade = 0
        else: 
            wrong_input = True
            return 'Wrong letter grade input'
        if wrong_input == False:
            self.addGrade((grade*int(credits)), int(credits))
        

def makeStudent(infoStr):
    # infoStr is a tab-separated line: bame hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split('\t')
    return Student(name, hours, qpoints)

def main():
    filename = input('Enter the name of the grade file: ')
    infile = open(filename, 'r')
    best = makeStudent(infile.readline())

    for line in infile:
        s = makeStudent(line)
        # if this student is best so far, remember it
        if s.gpa() > best.gpa():
            best = s
    infile.close()
    print('The best student is:', best.getName())
    print('Hours: {0}   GPA: {1}'.format(best.getHours(), best.gpa()))

if __name__ == '__main__':
    main()