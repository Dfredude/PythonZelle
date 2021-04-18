from graphics import *

def main():
    #Initialize graphic window
    win = GraphWin('Fahrenheit to Celsius converter', 720, 480)
    win.setCoords(0,0,10,10) #Set coordenates to our desire
    #Write texts
    Text(Point(5,9),'This program will convert from Farenheit to Celsius').draw(win)
    Text(Point(2.5,6),'Enter any value to convert: ').draw(win)
    Text(Point(2.5,3),'The result is: ').draw(win)

    #Get input
    inputText = Entry(Point(7, 6), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    #output
    outputText = Text(Point(7, 3),'')
    outputText.draw(win)
    #Convert button
    button = Text(Point(5,2.0), 'Convert it')
    button.draw(win)
    Rectangle(Point(4,1.5), Point(6, 2.5)).draw(win)
    
    #Wait for mouse click
    win.getMouse()
    #Convert Input
    Fahrenheit = float(inputText.getText())
    Celsius = (Fahrenheit-32)*5/9

    #Display output and change button
    outputText.setText(round(Celsius,2))
    button.setText('Quit')
    win.getMouse()

main()