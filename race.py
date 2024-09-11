import turtle 
import random 


x = -400
y = -100
endline = [400, (-150, 150)]
colors = ['red', 'yellow', 'green', 'navy', 'purple']
turtles = []

x_line = 400

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color('black')
turtle2.hideturtle()
turtle2.teleport(400, -100)
turtle2.left(90)

turtle.tracer(0,0)
for line in range(7):
    
    for i in range(30):
        turtle2.pendown()
        turtle2.fd(5)
        turtle2.up()
        turtle2.fd(5)

    x_line +=5
    turtle2.teleport(x_line, -100)


index = 0
for player in range(5): 
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.penup()
    turtle1.color(colors[index])
    y += 50
    turtle1.goto(x, y)
    index +=1
    turtles.append(turtle1)

turtle.tracer(1, 15)

while True:

    turtles[0].fd(random.randint(1, 30))
    turtles[1].fd(random.randint(1, 30))
    turtles[2].fd(random.randint(1, 30))
    turtles[3].fd(random.randint(1, 30))
    turtles[4].fd(random.randint(1, 30))
    if turtles[0].xcor() >= 400:
        winner = turtles[0]
        turtle2.write('Red Turtle Won')
        break
    elif turtles[1].xcor() >= 400:
        winner = turtles[1] 
        turtle2.write('yellow Turtle Won')
        break
    elif turtles[2].xcor() >= 400:
        winner = turtles[2] 
        turtle2.write('green Turtle Won')
        break
    elif turtles[3].xcor() >= 400:
        winner = turtles[3] 
        turtle2.write('navy Turtle Won')
        break
    elif turtles[4].xcor() >= 400:
        winner = turtles[4] 
        turtle2.write('purple Turtle Won')
        break    
    
    
    for tl in turtles:
        print(tl.xcor())
        x = int(tl.xcor())
        if x >= 400:
            winner = tl
            break
           







turtle.done()