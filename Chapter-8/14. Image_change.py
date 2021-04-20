from graphics import *

def sidebar(point_one, point_two, text, win):
    box = Rectangle(point_one, point_two)
    box.setFill('cyan')
    point_oneX = point_one.getX()
    point_oneY= point_one.getY()
    point_twoX = point_two.getX()
    point_twoY = point_two.getY()
    y_dif = point_twoY - point_oneY
    x_dif = point_twoX - point_oneX
    what_to_do_text = Text(Point(point_oneX + x_dif/2, point_oneY+y_dif/2), text)
    outputfile = Entry(Point(point_oneX+x_dif/2, point_oneY+y_dif/4), 10)
    box.draw(win)
    outputfile.draw(win)
    what_to_do_text.draw(win)
    key = False
    while key != 'Return':
        key = win.getKey()
        print(key)
    return outputfile.getText()

def main():
    img = Image(Point(0, 0), 'img2.gif')
    img_width = img.getWidth()
    img_height = img.getHeight()
    win = GraphWin('Change color', img_width, img_height)
    win.setCoords(0, 0, img_width, img_height)
    img.move(img_width/2, img_height/2)
    img.draw(win)
    for each_row in range(200):
        for each_column in range(200):
            r, g, b = img.getPixel(each_row, each_column)
            brightness = int(round(.299*r + .587*g + .114*b))
            img.setPixel(each_row, each_column, color_rgb(brightness, brightness, brightness))
        update()
    filename = sidebar(Point(0, img_height-img_height/15), Point(img_width, img_height), 'Enter the filename save and press Enter', win)
    img.save(filename)
    win.getMouse()
    
main()