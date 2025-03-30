
x=10
y=10
w=10
def setup():
    size(600, 400)
def draw():
    global x
    global y
    global w
    ellipse(y,w,x,x)
    stroke(60)
    x=x-1
    y=y+1
    w=w+1
    
