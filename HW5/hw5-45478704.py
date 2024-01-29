from graphics import *
import time
import random

class Car(Rectangle):
    def __init__(self, win, x, y, unit):
        colorlist = ["green",  "yellow", "red","purple",  "orange",  "blue"]
        #...
        self.color=random.choice(colorlist)
        self.x=x
        self.y=y
        self.unit=unit
        self.score=int(unit*10)
        p1=Point(x-(unit*4),y)
        p2=Point(x+(unit*8),y+(unit*3))
        p3=Point(x+(unit*4),y+(unit*4))
        self.drawCar(p1,p2,p3,win)

        super().__init__(p1,p2)



    def getColor(self):
        return self.color
    def getScore(self):
        return self.score
    def drawCar(self, p1, p2,p3, win):
        #...
        carlist1=[]
        self.tire_left = Circle(Point(p1.x + abs(p2.x - p1.x) / 4, p1.y), abs(p2.x - p1.x) / 8)
        self.tire_left.setFill("black")
        self.tire_left.draw(win)
        carlist1.append(self.tire_left)
        self.tire_right = Circle(Point(p2.x - abs(p2.x - p1.x) / 4, p1.y), abs(p2.x - p1.x) / 8)
        self.tire_right.setFill("black")
        self.tire_right.draw(win)
        carlist1.append(self.tire_right)
        self.body = Rectangle(p1, p2)
        self.body.setFill(self.color)
        self.body.draw(win)
        carlist1.append(self.body)
        width = abs(p2.x - p1.x) / 2
        height = abs(p2.y - p1.y)

        self.roof = Polygon(Point(p1.x + width / 2, p2.y), Point(p1.x + 3 * width / 4, p3.y),
                        Point(p2.x - 3 * width / 4, p3.y), Point(p2.x - width / 2, p2.y))
        self.roof.setFill("black")
        self.roof.draw(win)
        carlist1.append(self.roof)
        return carlist1

    def move(self, Xdistance):
        #...
        self.tire_right.move(Xdistance,0)
        self.tire_left.move(Xdistance,0)
        self.body.move(Xdistance,0)
        self.roof.move(Xdistance,0)
        super().move(Xdistance,0)
    def undraw(self):
        #...
        self.undraw()

def isClicked(pclick,rec):
    #...
    if rec.getP2().getX() > pclick.getX() > rec.getP1().getX() and rec.getP2().getY() > pclick.getY() > rec.getP1().getY():
        return True
    else:
        return False


def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

def main():
    win = GraphWin("Moving Cars", 800, 600)
    win.setCoords(0, 0, 40, 40)
    bg = Rectangle(Point(0,25), Point(40, 40))
    bg.setFill("light blue")
    bg.draw(win)
    ground = Rectangle(Point(0,6) , Point(40, 24))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4
    
    while temp<40:
        gnd_lines1= Line(Point(temp,10),Point(temp+4,10))
        gnd_lines1.setWidth(5)
        gnd_lines1.setFill("white")
        gnd_lines2= Line(Point(temp,15),Point(temp+4,15))
        gnd_lines2.setWidth(5)
        gnd_lines2.setFill("white")
        gnd_lines3= Line(Point(temp,20),Point(temp+4,20))
        gnd_lines3.setWidth(5)
        gnd_lines3.setFill("white")
        temp=temp+10
        gnd_lines1.draw(win)
        gnd_lines2.draw(win)
        gnd_lines3.draw(win)
    sun = Circle(Point(37,38), 1.5)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)
    with open('input.txt','r') as file:
     # reading each line
        for line in file:
            coordinates=[]
            # reading each word
            for word in line.split():
             # displaying the words
                coordinates.append(word)

            draw_buildings(win, coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4])
    button = Rectangle(Point(2,2), Point(6, 4))
    button.setFill("gray")
    button.draw(win)
    label = Text(Point(4, 3), "Start")
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)
    bottom_message = Text(Point(9, 5), "Please click the Start button to begin")
    bottom_message.setStyle("bold")
    bottom_message.setTextColor("green")
    bottom_message.draw(win)
    car_on_screen_message = Text(Point(15, 27), "")
    car_on_screen_message.setStyle("bold")
    car_on_screen_message.setTextColor("purple")
    car_on_screen_message.draw(win)
    score_title = Text(Point(15, 3), "Current Score: ")
    score_title.setStyle("bold")
    score_title.setSize(18)
    score_title.setTextColor("blue")
    score_title.draw(win)
    score_message = Text(Point(21, 3), "0")
    score_message.setStyle("bold")
    score_message.setSize(18)
    score_message.setTextColor("blue")
    score_message.draw(win)
    clicked_colors_message = Text(Point(29, 5),"")
    clicked_colors_message.setStyle("bold")
    clicked_colors_message.setTextColor("black")
    clicked_colors_message.draw(win)
    exit_bg = Rectangle(Point(10,5), Point(30, 20))
    exit_bg.setFill("light gray")
    exit_message = Text(Point(20, 15), "Click Exit to Stop Playing \n or Resume to continue")
    exit_message.setSize(18)
    exit_message.setStyle("bold")
    exit_message.setTextColor("red")
    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
    confirm_button.setFill("gray")
    confirm_label = Text(Point(15, 8), "Exit")
    confirm_label.setStyle("bold")
    confirm_label.setTextColor("white")
    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill("gray")
    go_back_label = Text(Point(25, 8), "Resume")
    go_back_label.setStyle("bold")
    go_back_label.setTextColor("white")
    mylabel=Text(Point(26,3),"Clicked Color:")
    mylabel.setStyle("bold")
    mylabel.draw(win)
    myrectangle=Rectangle(Point(29,2),Point(31,4))
    myrectangle.draw(win)
    pixel_per_second =10
    refresh_sec = 0.05
    gameState = 0 # 0 for initial mode, 1 for start mode, 2 for pause mode
    total_score = 0
    car_list = []
    clicked_colors = {}
    start_time1 = 0
    start_time2 = 0


    while True:
        #...
        time.sleep(0.0001)
        # c=0


        pClick=win.checkMouse()

        if gameState == 0: #initial
            time.sleep(0.1)
            if pClick != None:
                if isClicked(pClick, button):
                    #...
                    bottom_message.undraw()
                    bottom_message = Text(Point(10, 5), "Please click a moving car or Pause to stop")
                    bottom_message.setStyle("bold")
                    bottom_message.setTextColor("green")
                    bottom_message.draw(win)
                    label.setText("Pause")
                    gameState=1

        elif gameState == 1: # start
            if pClick != None:
                if isClicked(pClick, button):
                    #...
                    gameState=2
                    exit_bg.draw(win)
                    exit_message.draw(win)
                    confirm_button.draw(win)
                    confirm_label.draw(win)
                    go_back_button.draw(win)
                    go_back_label.draw(win)
                else:
                    for r in car_list:
                        if isClicked(pClick,r):
                            car_color = r.getColor()
                            temp = r.getScore()
                            if str(car_color) in clicked_colors:
                                clicked_colors[car_color]+=1
                            else:
                                clicked_colors[car_color]=1
                            r.tire_left.undraw()
                            r.tire_right.undraw()
                            r.body.undraw()
                            r.roof.undraw()
                            car_list.remove(r)

                            color_counter=clicked_colors.get(car_color,0)+1
                            bonus=int(100*(1/temp))
                            total_score+=bonus
                            score_message.setText(total_score)
                            myrectangle.setFill(car_color)


            #...
            text_messages=[]
            for i,k in enumerate(clicked_colors):
                appended=(k)+" "+str(clicked_colors[k])

                text_messages.append(appended)

            joined_list=", ".join(text_messages)
            clicked_colors_message.setText(str(joined_list))


            
            # if the gen time lag is greater than 1, then generate a new car
            # and reset timer for car generation
            current_time = time.time()
            if (current_time - start_time1) >= 0.1:
                #...
                x=random.uniform(3.5,4.5)
                y=random.uniform(7,23)
                unit=random.uniform(0.4,1)
                racecar=Car(win,x,y,unit)
                car_list.append(racecar)
                start_time1=current_time+1

            # if moving time lag is greater than refesh,
            # set proportional distance to the lag. Then check whether car goes outside window
            if current_time - start_time2 >= refresh_sec:
                #...
                for n in car_list:
                    n.move(pixel_per_second*refresh_sec)

                    if n.getP2().getX()>800:
                        n.undraw()
                        car_list.remove(n)

                    start_time2=current_time
           
        elif gameState == 2: # pause
            time.sleep(0.1)
            if pClick != None:
                if isClicked(pClick, confirm_button):
                    #...
                    win.close()
                    break

                            
                elif isClicked(pClick, go_back_button):

                    exit_bg.undraw()
                    exit_message.undraw()
                    confirm_button.undraw()
                    confirm_label.undraw()
                    go_back_button.undraw()
                    go_back_label.undraw()
                    gameState=1
                    #...
                    start_time1=time.time()
                    start_time2=time.time()

if __name__ == '__main__':
    main()
