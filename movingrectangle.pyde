c=color(0)
x=0.0
y=200.0
speed=1.0

def setup():
    size(400,300,P3D);
def draw():
    background(255)
    move()
    display()
    #rect(30,20,mouseX,mouseY)
def move():
    global x
    x=x+speed
    if x>width:
        x=0       
def display():
    fill(c)
    rect(x,y,40,20)         
