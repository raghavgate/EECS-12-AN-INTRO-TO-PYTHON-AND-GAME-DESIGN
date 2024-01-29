


from graphics import *
from time import *
import random

#given top and lower left corner, draw the tires and car body
def draw_car(win,p1,p2):
    carlist1=[]
    tire_left= Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
    tire_left.setFill("black")
    tire_left.draw(win)
    carlist1.append(tire_left)
    tire_right= Circle(Point(p2.x-abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
    tire_right.setFill("black")
    tire_right.draw(win)
    carlist1.append(tire_right)

    body=Rectangle(Point(p1.x, p1.y),Point(p2.x, p2.y))
    body.setFill("blue")
    body.draw(win)
    carlist1.append(body)
    return carlist1

def draw_vehicle_roof(win, p1, p2, p3, cartype):
    carlist=[]
    if cartype == 1:
        width = abs(p2.x - p1.x)
        roof = Polygon(Point(p1.x + width/4, p2.y), Point(p2.x - width/4, p2.y), Point(p2.x - 3 * width/8, p3.y), Point(p1.x + 3 * width/8, p3.y))
        roof.setFill("red")
        roof.draw(win)
        carlist.append(roof)

    elif cartype == 2:
        width = abs(p2.x - p1.x)
        roof = Rectangle(Point(p2.x, p2.y), Point(p2.x - width/2, p3.y))
        roof.setFill("orange")
        roof.draw(win)
        carlist.append(roof)

    return carlist

def draw_truck(win,p1,p2):
    buslist=[]
    
    tire_left= Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
    tire_left.setFill("black")
    tire_left.draw(win)
    buslist.append(tire_left)

    tire_right= Circle(Point(p2.x-abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
    tire_right.setFill("black")
    tire_right.draw(win)
    buslist.append(tire_right)

    body=Rectangle(Point(p1.x, p1.y),Point(p2.x, p2.y))
    body.setFill("yellow")
    body.draw(win)

    buslist.append(body)
    
    
    return buslist

def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

def createButtons(win, anchor, width, height):
    button_list = [ ]
    label = ["Day", "Night", "Speed-Up", "Exit"]

    for i in range(4):
        anchor1 = anchor.clone()
        anchor2 = anchor.clone()
        anchor2.move(width, height)
        newbutton = Rectangle(anchor1, anchor2)
        newbutton.setFill("gray")
        newbutton.draw(win)
        anchor1.move(width/2, height/2)
        newlabel = Text(anchor1, label[i])
        newlabel.setStyle("bold")
        newlabel.setTextColor("white")
        newlabel.draw(win)
        if i==2:
            newlabel_special=newlabel
        button_list.append(newbutton)
        anchor.move(width+1, 0)

    return button_list, newlabel_special

def isHitBtn(pclick, btn):
    if pclick.getX()>btn.p1.x and pclick.getX()<btn.p2.x and pclick.getY()>2 and pclick.getY()<4:
        return True
    return False

def main():
    win = GraphWin("City View!", 800, 600)
    win.setCoords(0, 0, 40, 30)

    bg = Rectangle(Point(0,15), Point(40, 30))
    bg.setFill("light blue")
    bg.draw(win)

    ground = Rectangle(Point(0,6) , Point(40, 14))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4

    while temp<40:
        gnd_lines = Line(Point(temp,10), Point(temp+4, 10))
        gnd_lines.setWidth(5)
        gnd_lines.setFill("white")      
        gnd_lines.draw(win)
        temp+=10
        

    sun = Circle(Point(37,27), 2)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)
    
    
    moon = Circle(Point(37, 27), 2)
    moon.setFill("white")
    moon.setOutline("white")
    

    phase = Circle(Point(37.75, 28), 1.5)
    phase.setFill("navy")
    phase.setOutline("navy")
   

    with open('input.txt','r') as file:
     # reading each line in the file
        for line in file:
            x=line.split()
            x1=x[0]
            y1=x[1]
            x2=x[2]
            y2=x[3]
            color=x[4]
            draw_buildings(win,x1,y1,x2,y2,color)
        file.close()

    txtMsg1 = Text(Point(20, 29), "Sunny Day")
    txtMsg1.setStyle("bold")
    txtMsg1.setTextColor("orange")
    txtMsg1.draw(win)

    # === set text for asking user to click a point ===
    pntMsg = Point(20, 5)
    txtMsg = Text(pntMsg, "Please click the left bottom point of the car body.")
    txtMsg.setStyle("bold")
    txtMsg.setTextColor("red")
    txtMsg.draw(win)
    # === get the point from mouse ===
    p1 = win.getMouse()
    txtMsg.setText("Now click the upper right point of the car body.")

    p2 = win.getMouse()
    e1=draw_car(win, p1, p2)
    # === change the text to ask user to click another point ===
    txtMsg.setText("Now click the top point of the car.")

    p3 = win.getMouse()
    e2=draw_vehicle_roof(win, p1, p2, p3, 1)
    txtMsg.setText("Now click the lower left point of the truck body.")
    p1 = win.getMouse()
    txtMsg.setText("Now click the upper right point of the truck body.")
    p2 = win.getMouse()
    e1=draw_truck(win, p1, p2)
    txtMsg.setText("Now click the roof top point of the truck.")
    p3 = win.getMouse()
    txtMsg.undraw()
    e2=draw_vehicle_roof(win, p1, p2, p3, 2)
    buttons,special_label = createButtons(win, Point(2,2), 4, 2)
    gameState = 0 # 0 for sunny day, 1 for moon night, 2 for sunny windy day, 3 for moon windy night
    speed = 0.05 #This speed is a variable that you can tune to see differences in speed

    while True:
        sleep(0.0001)
        for part in e1:
            part.move(speed, 0)
            if part.getP1().getX() > 40:
                part.move(-2-part.getP1().getX(), 0)

        for part in e2:
            part.move(speed, 0)
            if part.getP2().getX() > 40:
                part.move(-2-part.getP2().getX(), 0)

        pClick = win.checkMouse()
        if pClick is not None:
            if isHitBtn(pClick, buttons[3]): #Exit
                win.close()

            elif isHitBtn(pClick, buttons[0]): #Day
                if gameState == 2:
                    speed = 0.3
                elif  gameState == 3:
                    sun.undraw()
                    gameState = 2
                    speed = 0.3
                    bg.setFill("light blue")
                    moon.undraw()
                    phase.undraw()
                    sun.draw(win)
                else:
                    sun.undraw()
                    gameState = 0
                    speed = 0.05
                    bg.setFill("light blue")
                    moon.undraw()
                    phase.undraw()
                    sun.draw(win)

            elif isHitBtn(pClick, buttons[1]): #Night
                if gameState == 3:
                    speed = 0.15
                elif gameState == 2:
                    moon.undraw()
                    phase.undraw()
                    gameState = 3
                    speed = 0.15
                    bg.setFill("navy")
                    sun.undraw()
                    moon.draw(win)
                    phase.draw(win)
                else:
                    moon.undraw()
                    phase.undraw()
                    gameState = 1
                    speed = 0.05
                    bg.setFill("navy")
                    sun.undraw()
                    moon.draw(win)
                    phase.draw(win) 

            elif isHitBtn(pClick, buttons[2]): #speed-up/slow down
                if gameState == 0:
                    gameState = 2
                    speed = 0.3
                    special_label.setText("Slow-Down")
                elif gameState == 2:
                    gameState = 0
                    speed = 0.05
                    special_label.setText("Speed-Up")
                elif gameState == 1:
                    gameState = 3
                    speed = 0.15
                    special_label.setText("Slow-Down")
                elif gameState == 3:
                    gameState = 1
                    speed = 0.05
                    special_label.setText("Speed-Up")



            if gameState == 0: txtMsg1.setText("Sunny Day")
            elif gameState == 1: txtMsg1.setText("Moon Night")
            elif gameState == 2: txtMsg1.setText("Sunny Day, High Speed")
            elif gameState == 3: txtMsg1.setText("Moon Night, Medium Speed")

main()
    

