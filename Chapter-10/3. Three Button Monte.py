from graphics import *
from widgets import Door, Button
from random import randrange

def main():
    playing = True
    win = GraphWin('Three Button Monte', 1280, 720)
    win.setCoords(0,0,100,100)
    Text(Point(50, 85), 'Open a door by clicking on it').draw(win)
    while playing == True:
        door1, door2, door3 = Door(Point(25, 45), win, 20, 45, 1), Door(Point(50, 45), win, 20, 45, 2), Door(Point(75, 45), win, 20, 45, 3)
        doors = [door1, door2, door3]
        door_chosen = randrange(0,3)
        doors[door_chosen].activate()
        doorclicked = waitForClick(win, doors)
        print(doorclicked, door_chosen)
        if doors[doorclicked-1].getActive() == True:
            result_text = Text(Point(50, 75), 'You won').draw(win)
        else:
            result_text = Text(Point(50, 75), 'You lost').draw(win)
        doors[doorclicked-1].openDoor()
        play_again_button = Button(win, Point(25, 10), 20, 15, 'Play again')
        quit_button = Button(win, Point(75, 10), 10, 15, 'Quit')
        play_again_button.activate()
        quit_button.activate()
        buttonclicked = False
        while buttonclicked != True:
            click = win.getMouse()
            if play_again_button.clicked(click):
                play_again_button.deactivate()
                quit_button.deactivate()
                for door in doors: door.undraw()
                buttonclicked = True
                result_text.undraw()
            elif quit_button.clicked(click):
                playing = False
                win.close()

            

def waitForClick(win, doors):
    clicked = False
    while clicked == False:
        click = win.getMouse()
        clickX, clickY = click.getX() , click.getY()
        for door in doors:
            if ((door.getX()-(door.getWidth()/2)) <= clickX <= (door.getX()+(door.getWidth()/2))
            and (door.getY()-(door.getHeight()/2)) <= clickY <= (door.getY()+(door.getHeight()/2))):
                door_clicked = door
                clicked = True
    return door_clicked.getDoorNum()


main()
