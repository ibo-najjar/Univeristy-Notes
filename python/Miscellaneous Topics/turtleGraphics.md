<div class="cell code" data-execution_count="3">

``` python
import turtle
```

</div>

<div class="cell code" data-execution_count="6">

``` python
def DrawRectangle(t,x,y,w,h,colorP="black"):
    t.pencolor(colorP)
    t.up()
    t.goto(x,y)
    t.down()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)
t = turtle.Turtle()
DrawRectangle(t,0,0,100,100)
```

</div>

<div class="cell code" data-execution_count="2">

``` python
def DrawRectangle(t,x,y,w,h,colorP="black"):
    t.clear()
    t.pencolor(colorP)
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
t = turtle.Turtle()
DrawRectangle(t,0,0,100,100)
```

</div>

<div class="cell code" data-execution_count="6">

``` python
def main():
    t = turtle.Turtle()
    t.hideturtle()
    DrawRectangle(t, 0, 0, 100, 150, "blue", "grey")
def DrawRectangle(t,x,y,w,h,colorP="black",colorF="white"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x,y)
    t.begin_fill()
    t.down()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)
    t.end_fill()
main()
```

</div>

<div class="cell code">

``` python
import turtle
def main():
    t = turtle.Turtle()
    t.hideturtle()
    
```

</div>

<div class="cell code">

``` python
import turtle
wn=turtle.Screen()
wn.bgcolor("white")
from turtle import *
prev=0
start=1
fibonacci=1
sqs = input("How many Squares do you want?")
for i in range(int(sqs)):
    print(str(i)+". "+str(fibonacci))
    color('black')
    for f in range(6):
        forward(5*fibonacci)
        if f<5:right(90)

    fibonacci=start+prev
    prev=start
    start=fibonacci
```

</div>
