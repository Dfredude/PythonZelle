from graphics import *
from math import *

def main():
    #Open file
    file_name = input('Enter filename: ')
    infile = open(file_name, "r")
    #Read first line that contains number of students
    studentsline = infile.readline()
    students = studentsline.split()
    nstudents = int(students[0]) #Number of students
    #Read all lines
    lines = (infile.readlines())
    #Get y length for each space
    length_space = int(floor(100/nstudents))
    #Initialize graphical window
    win = GraphWin('Score graph program', 1280, nstudents*70)
    win.setCoords(0, 100, 100, 0)
    #Loop and draw each score
    for i in range(nstudents+1):
        if i == 0:
            pass
        else:
            #Define variables
            print(lines)
            line = (lines[i-1])
            print(line)
            sepline = line.split()
            print(sepline)
            score = int(sepline[1])
            name = sepline[0]
            #Build scorebar
            scorebar = Rectangle(Point(20, ((i-1)*length_space)), Point((score*.9), ((i)*length_space)-2))
            scorebar.setFill('Blue')
            #Build name text
            name_text = Text(Point(10, (i*length_space-(length_space/2))), name)
            #Draw shit
            scorebar.draw(win)
            name_text.draw(win)
    win.getMouse()



main()