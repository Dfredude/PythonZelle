from gpa import Student, readStudents, writeStudents

def main():
    print('This program sorts student grade information by GPA, name or credits')
    filename = input('Enter a name for the data file: ')
    sort_option = str(input('How do you want to order them? (GPA, name, credits): '))
    sort_option = sort_option.lower()
    reverse = str(input('In reverse order? (Y/N)')).lower()
    if reverse == 'n' or reverse == 'no' or reverse == '': reverse = False
    else: reverse = True
    data = readStudents(filename)
    if sort_option == 'gpa': data.sort(key=Student.gpa, reverse = reverse)
    elif sort_option == 'name': data.sort(key = Student.getName, reverse = reverse)
    elif sort_option == 'credits': data.sort(key = Student.getQPoints(), reverse = reverse)
    filename = input('Enter a name for the output file: ')
    writeStudents(data, filename)
    print('The data has been written to', filename)

if __name__ == '__main__': main()