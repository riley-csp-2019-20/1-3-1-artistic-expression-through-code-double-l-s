import turtle as trtl
import math 

wn = trtl.Screen()
wn.bgcolor("white")
wn.setup(700,700)
font = ("Comic sans", 35, "bold")
t = trtl.Turtle()


#Creates the pen - Christian Thompson https://christianthompson.com

class Pen(trtl.Turtle):
    def __init__(self):
        trtl.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.pu()
        self.speed(0)

#Creates the letter - Christian Thompson

class Player(trtl.Turtle):
    def __init__(self):
        trtl.Turtle.__init__(self)
        self.shape("square")
        self.color("cyan")
        self.pu()
        self.speed(0)
#Movement Function
    def go_up(self):
      move_to_x = player.xcor()
      move_to_y = player.ycor() + 24
      if (move_to_x, move_to_y) not in walls:
          self.goto(move_to_x, move_to_y)
    
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

def is_collision(self, other):
    a = self.xcor()-other.xcor()
    b = self.ycor()-other.ycor()
    distance = math.surt((a**2) + (b**2))

    if distance < 5:
        return True
    else:
        return False

'''class treasure(trtl.Turtle):
    def __init__(self, x, y):
        trlt.Turtle.__init__(self)
        self.shape("turtle")
        self.color("gold")
        self.pu()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.ht()'''

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX         XXXXXX",
"X  XXXXXXX  XXXXX  XXXXXX",
"X       XX  XXXXX  XXXXXX",
"XX      XX  XXX        XX",
"XXXXXX  XX  XXXXX  XXXXXX",
"XXXXXX  XX  XXXXX  XXXXXX",
"XXXXXX  XX    XXXXXXXXXXX",
"X  XXX        XXXXXXXXXXX",
"X  XXXXXXXXX    XXXXXXXXX",
"X         XX    XXXXXXXXX",
"X               XXXXXXXXX",
"XXXXXXXXXX  XX   XXXXXXXX",
"XXXXXXXXXX  XX   XXXXXXXX",
"X           XX          X",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXX   XXXX",
"X              XXX   XXXX",
"X   XXXXXXXX   XXX   XXXX",
"X   XXXXXXXX         XXXX",
"X   XXXXXXXX   XXXXXXXXXX",
"X   XXXXXXXX   XXXXXXXXXX",
"X   XXXXXXXX            X",
"X   XXXXXXXX       T    X",
"X   XXXXXXXX   XXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Treasure list
#treasures = []
#Adding the maze to maze list
levels = [""]
levels.append(level_1)

#Creating level -Christian Thompson https://christianthompson.com

def start_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Gets letter coordinates
            letter = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = -288 + (y * 24)

            #Creating walls
            if letter == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
            #Wall Collision
                walls.append((screen_x , screen_y))


            #Spawns letter
            if letter == "P":
                 player.goto(screen_x,screen_y)
            '''if letter == "T":
                treasure.append(treasure(screen_x,screen_y))
'''

timer = 5
t_interval = 1000  
timer_up = False

t.ht()
t.up()
t.goto(300,350)
t.speed(0)
t.down()

def countdown():
  global timer, timer_up
  t.clear()
  if timer <= 0:
    t.write("Time's Up", font=font)
    timer_up = True
    game_over()
  else:
    t.write("Timer: " + str(timer), font=font)
    timer -= 1
    t.getscreen().ontimer(countdown, t_interval)

def game_over(): 
    t.ht()
    t.up()
    t.goto(-450,350)
    t.down()
    t.write("Game over. Great Job!", font = font)


#Create class

pen = Pen()
player = Player()

#Creates wall list
walls = [""]

#Set up level

start_maze(levels[1])
print(walls)
#Key bindings

wn.listen()
trtl.onkey(player.go_left, "Left")
trtl.onkey(player.go_right, "Right")
trtl.onkey(player.go_up, "Up")
trtl.onkey(player.go_down, "Down")

wn. tracer(0)
wn.ontimer(countdown, t_interval) 
'''while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold.{}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)'''

while True:
    wn.update()
