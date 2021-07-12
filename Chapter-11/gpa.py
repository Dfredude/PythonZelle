#gpa.py

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

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print('{0}\t{1}\t{2}'.format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)
    outfile.close()

def main():
    print('This program sorts student grade information by GPA')
    filename = input('Enter a name for the data file: ')
    data = readStudents(filename)
    print(data)
    data.sort(key=Student.gpa, reverse = True)
    print(data)
    filename = input('Enter a name for the output file: ')
    writeStudents(data, filename)
    print('The data has been written to', filename)

if __name__ == '__main__':
    main()