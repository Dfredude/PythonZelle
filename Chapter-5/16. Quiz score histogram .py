#This program plots student exam scores on a horizontal bar chart
#open student_test.txt
from graphics import *
def createNum(number, x, y):
    numtext = Text(Point(x, y), str(number))
    return numtext

def createBar(iteration, y, h):
    num_bar = Rectangle(Point((iteration*10+4), y ), Point((iteration*10+6), 10+h))
    return num_bar 

def main():
    #Open file and read
    file_name = input('Enter file name: ')
    infile = open(file_name, 'r')
    lines = infile.readlines()
    #Convert string list to int list
    int_list = []
    for i in lines:
        int_list.append(int(i))
    numbers_list = [0,0,0,0,0,0,0,0,0,0,0]
    #Add up quantity of each number
    for i in int_list:
        if i == 0:
            numbers_list[0] += 1
        elif i == 1:
            numbers_list[1] += 1
        elif i == 2:
            numbers_list[2] += 1
        elif i == 3:
            numbers_list[3] += 1
        elif i == 4:
            numbers_list[4] += 1
        elif i == 5:
            numbers_list[5] += 1
        elif i == 6:
            numbers_list[6] += 1
        elif i == 7:
            numbers_list[7] += 1
        elif i == 8:
            numbers_list[8] += 1
        elif i == 9:
            numbers_list[9] += 1
        elif i == 10:
            numbers_list[10] += 1
        else:
            print('The number obtained ' + i + 'is not valid and is going to be skipped')
    #Draw window
    win = GraphWin('Scores tendency', 1280, 720)
    
    win.setCoords(0,0,110,110)
    #Define multiplier
    multiplier = 5
    if max(numbers_list) <= 10:
        multiplier = 10
    elif max(numbers_list) < 20 and max(numbers_list) > 10 :
        multiplier = 7
    elif max(numbers_list) >= 20:
        multiplier = 3
    for i in range(0, 11):
        number_text = createNum(i, i*10+5, 5)
        number_text.draw(win)
        h = (numbers_list[i]*multiplier) 
        bar = createBar(i, 10, h)
        bar.draw(win)
        
    print(numbers_list)
    win.getMouse()
    

main()