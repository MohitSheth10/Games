import turtle as t
crosses=[]
circles=[]
t.speed(0)
t.hideturtle()
t.bgcolor("cyan")
t.pencolor("black")
t.penup()
t.goto(-150,150)
t.pendown()
def circle():
    t.tracer(0, 0)
    t.pensize(5)
    t.left(90)
    t.forward(28.65)
    t.right(90)
    t.speed(0)
    t.pendown()
    for i in range(0,360):
        t.forward(0.5)
        t.right(1)
    t.right(90)
    t.penup()
    t.forward(28.65)
    t.left(90)
    t.update()
    t.tracer(1)
def cross():
    t.pendown()
    t.pensize(6)
    t.left(45)
    t.forward(40)
    t.back(80)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.back(80)
    t.forward(40)
    t.right(135)
    t.penup()
def square():
    for i in range(3):
        for i in range(1,5):
            t.forward(100)
            t.right(90)
        t.forward(100)
square()
t.penup()
t.goto(-150,50)
t.pendown()
square()
t.penup()
t.goto(-150,-50)
t.pendown()
square()
positions = {
    1: (-140, 120),
    2: (-40, 120),
    3: (60, 120),
    4: (-140, 20),
    5: (-40, 20),
    6: (60, 20),
    7: (-140, -80),
    8: (-40, -80),
    9: (60, -80)
}  
t.pencolor("black")
t.penup()
t.goto(0,0)
winning_combinations = [
    [1, 2, 3],   
    [4, 5, 6],  
    [7, 8, 9],  
    [1, 4, 7],  
    [2, 5, 8],  
    [3, 6, 9], 
    [1, 5, 9],  
    [3, 5, 7]  
]
i=0
tp=0
result=None

def my_click_function(x, y):
    global i, tp, result
    if 50 < y <= 150:
        y = 100
        if -150 <= x < -50:
            x = -100
            choice = 1
        elif -50 <= x < 50:
            x = 0
            choice = 2
        elif 50 <= x <= 150:
            x = 100
            choice = 3
        else:
            print("x coord Out of Range")
            return
    elif -50 < y <= 50:
        y = 0
        if -150 <= x < -50:
            x = -100
            choice = 4
        elif -50 <= x < 50:
            x = 0
            choice = 5
        elif 50 <= x <= 150:
            x = 100
            choice = 6
        else:
            print("x coord Out of range")
            return
    elif -150 <= y <= -50:
        y = -100
        if -150 <= x < -50:
            x = -100
            choice = 7
        elif -50 <= x < 50:
            x = 0
            choice = 8
        elif 50 <= x <= 150:
            x = 100
            choice = 9
        else:
            print("x coord Out of range")
            return
    else:
        print("y coord Out of range")
        return
    
    # Ignore if spot already taken
    if choice in crosses or choice in circles:
        print("Spot already taken!")
        return
    
    t.goto(x, y)
    
    if i % 2 == 0:
        print("Player A: ")
        circles.append(choice)
        circle() 
    else:
        print("Player B:")
        crosses.append(choice)
        cross() 
    
    i += 1
    
    for combo in winning_combinations:
        if all(num in circles for num in combo):
            t.penup()
            t.pencolor("red")
            t.goto(-140,200)
            t.pendown()
            t.write("Player A WINS", font=("Arial", 32, "bold"))
            t.onscreenclick(None)
            return
    for combo in winning_combinations:
        if all(num in crosses for num in combo):
            t.penup()
            t.pencolor("red")
            t.goto(-140,200)
            t.pendown()
            t.write("Player B WINS", font=("Arial", 32, "bold"))
            t.onscreenclick(None)
            return
    
    if i == 9:
        t.penup()
        t.pencolor("red")
        t.goto(-40,180)
        t.pendown()
        t.write("TIE!", font=("Arial", 32, "bold"))
        t.onscreenclick(None)

t.onscreenclick(my_click_function)

t.done()
