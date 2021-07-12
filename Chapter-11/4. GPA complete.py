from graphics import GraphWin, Point, Text
from gpa import Student, readStudents, writeStudents
from tkinter.filedialog import askopenfilename, asksaveasfilename
from widgets import Button

def createWindow():
    win = GraphWin('Sort Students', 720, 480)
    win.setCoords(0,0,100,100)
    return win
    
def deactivateAll(*args):
    for arg in args:
        arg.deactivate()

def main():
    win = createWindow()
    #Create all buttons
    openButton = Button(win, Point(20, 75), 10, 5, 'Open')
    openButton.activate()
    GPAButton = Button(win, Point(70, 60), 10, 5, 'GPA')
    nameButton = Button(win, Point(70, 50), 10, 5, 'Name')
    creditsButton = Button(win, Point(70, 40), 10, 5, 'Credits')
    reverseButton = Button(win, Point(20, 40), 10, 5, 'Reversed')
    sortButton = Button(win, Point(50, 20), 10, 5, 'Sort!')
    sortButton.activate()
    #Some text
    sortby_text = Text(Point(70, 75), 'Sort by:')
    sortby_text.draw(win)
    Description = Text(Point(50, 95),'This program sorts student grade information by GPA, name or credits').draw(win)
    #Create sorting options list
    sorting_buttons = [GPAButton, nameButton, creditsButton]
    #Wait for user interaction and execute proper command
    print(sorting_buttons[0], sorting_buttons[0].active)
    while True:
        click = win.getMouse()
        if openButton.clicked(click): 
            filename = askopenfilename()
        elif reverseButton.clicked(click):
            if reverseButton.active: 
                reverseButton.deactivate()
            else: 
                reverseButton.activate()
        elif sortButton.clicked(click):
            data = readStudents(filename)
            if sorting_buttons[0].active: data.sort(key = Student.getName, reverse = reverseButton.active)
            elif sorting_buttons[1].active: data.sort(key = Student.getName, reverse = reverseButton.active)
            elif sorting_buttons[2].active: data.sort(key = Student.getQPoints, reverse = reverseButton.active)
            output_filename = asksaveasfilename()
            writeStudents(output_filename)
        else:
            for button in sorting_buttons:
                if button.clicked(click) == True:
                    deactivateAll(*sorting_buttons)
                    button.activate()
                    print('Click')
    
    
    

if __name__ == '__main__': main()