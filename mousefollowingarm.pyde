x=100;
y=100;
angle1=0.0;
segLength=50;
def setup():
    size(700,500);
    strokeWeight(20);
    stroke(255,100);
def draw():
    global x;
    global y;
    background(0);
    dx=mouseX-x;
    dy=mouseY-y;
    angle1=atan2(dy,dx);
    x=mouseX-(cos(angle1) * segLength);
    y=mouseY-(sin(angle1) * segLength);
    segment(x,y,angle1);
    ellipse(x,y,20,20);
def segment(x,y,a):
    pushMatrix();
    translate
    line(mouseX,mouseY,x,y);
    popMatrix();
        
