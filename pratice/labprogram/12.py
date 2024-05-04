import turtle
def srp(t,x,y,size,depth,cahnge_depth):
    if depth==0:
        t.penup()
        t.goto(x, y)
        t.pendown()
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        srp(t, x, y, size/2, depth-1, change_depth)
        srp(t, x+size/2, y, size/2, depth-1, change_depth)
        srp(t, x+size/4, y+(size/2)*(3**0.5)/2, size/2, depth-1, change_depth)

        if depth==cahnge_depth:
            t.fillcolor('magenta')
            t.begin_fill()
            srp(t, x+size/4, y+(size/2)*(3**0.5)/2, size/2, 0, change_depth)
            t.end_fill()

            t.fillcolor('red')
            t.begin_fill()
            srp(t, x, y, size/2, 0, change_depth)
            t.end_fill()

            t.fillcolor('blue')
            t.begin_fill()
            srp(t, x+size/2, y, size/2, 0, change_depth)
            t.end_fill()
t=turtle.Turtle()
t.speed(0) 

change_depth=1

srp(t,-200,-200,300,4,change_depth)

turtle.done()

