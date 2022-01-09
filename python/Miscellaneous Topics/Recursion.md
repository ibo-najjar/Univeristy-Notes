<div class="cell code" data-execution_count="9">

``` python
def power(r,n):
    value = 1
    for i in range(1, n + 1):
        value = r * value
    return value
print(power(2,3))

def recursionPower(r, n):
    L = [r]
    if n == 1:
        return r
    else:
        print(f"{r}*"*(n-1),end="")
        print(r)
        return r * power(r,n-1)
print(recursionPower(2,7))
```

<div class="output stream stdout">

    8
    2*2*2*2*2*2*2
    128

</div>

</div>

<div class="cell code" data-execution_count="19">

``` python
def isPalindrome(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]: #first and last letters match
        word = word[1:-1] # remove first and last letters
        return isPalindrome(word)
    else:
        return False
word = "kayak"
d = "Palindrome" if isPalindrome(word) else "not Palindrome"
print(d)
```

<div class="output stream stdout">

    Palindrome

</div>

</div>

<div class="cell code">

``` python
import turtle

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    level = 12
    fract(t, -80, 60, 80, 60, level)

def fract(t, x1,y1,x2,y2,level):
    newX = 0
    newY = 0
    if level == 0:
        drawLine(t, x1,y1,x2,y2)
    else:
        newX = (x1+x2) + (y2-y1)/2
        newY = (y1+y2) + (x2-x1)/2
        fract(t,x1,y1,newX,newY, level-1)
        fract(t,newX,newY,x2,y2,level -1)
def drawLine(t,x1,y1,x2,y2):
    # draw line from (x1,y1) to (x2,y2)
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
main()
```

</div>
