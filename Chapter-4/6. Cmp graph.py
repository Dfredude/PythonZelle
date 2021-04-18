from graphics import *
def main():
    #Creates Graphical window
    win = GraphWin('Compound rate',720,720)
    win.setCoords(0,0,100,100)  #Sets the coordenates

    #Draw main text
    main_text = Text(Point(50, 95),"This is a program that calculates the future value of a 10 years investment.")
    main_text.draw(win)

    #Enter principal
    prp_text = Text(Point(50,85),'Enter the principal: ')
    prp_text.draw(win)
    prp  = Entry(Point(50,80), 5)
    prp.setText('0.0')
    prp.draw(win)
    
    #Enter annual percentage
    apr_text = Text(Point(50,70),'Enter the annual percentage rate(i.e .03 for 3%): ')
    apr_text.draw(win)
    apr  = Entry(Point(50,65), 5)
    apr.setText('0.0')
    apr.draw(win)

    #Enter button
    button_text_Y_point = 55
    button_text_X_point = 50
    button_text = Text(Point(button_text_X_point, button_text_Y_point),'Get result')
    button_text.draw(win)
    
    y_top = button_text_Y_point + 2.5
    y_bottom = button_text_Y_point - 2.5 
    button = Rectangle(Point(45,y_bottom),Point(55,y_top))
    button.draw(win)
    
    for i in range(20):
        click = win.getMouse()
        xcor = click.getX()
        ycor = click.getY()
        if xcor <= 55 and xcor >=45 and ycor <= y_top and ycor >= y_bottom:
            #Convert data to float
            prpft = float(prp.getText())
            aprft = float(apr.getText())
            #Draw labels on left
            labels(win)
            #Draw first bar
            height = prpft*.005
            first_bar_X_cord = 25
            first_bar = Rectangle(Point(first_bar_X_cord,5),Point(30,5+height))
            first_bar.setFill('Blue')    
            first_bar.draw(win)

            for j in range(10):
                prpft = prpft*(1+aprft)
                height = prpft*.005
                bar = Rectangle(Point(first_bar_X_cord+5,5),Point(first_bar_X_cord+10,height+5))
                bar.setFill('Blue')
                bar.draw(win)
                first_bar_X_cord = first_bar_X_cord + 5
            output_text = Text(Point(50, 45),'The result in 10 years is: ')
            output_text.draw(win)
            output_result = Text(Point(50, 42.5), str(prpft))
            output_result.draw(win)  
            win.getMouse()
            win.close()

def labels(window):
    Text(Point(15,30),'5K').draw(window)
    Text(Point(15,25),'4K').draw(window)
    Text(Point(15,20),'3K').draw(window)
    Text(Point(15,15),'2K').draw(window)
    Text(Point(15,10),'1K').draw(window)
    Text(Point(15,5),'0').draw(window)

main()
