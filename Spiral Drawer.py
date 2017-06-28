import turtle
T=turtle.Turtle
A = 1
turtle.speed = 10000000
lencount = 1
angcount = 1
while A == 1:
    angcount = angcount + 1
    if angcount == 20:
        angcount = 1
    lencount = lencount + 1
    if lencount == 25:
        lencount = 1
    turtle.forward(lencount)
    turtle.left(angcount)
    
    



