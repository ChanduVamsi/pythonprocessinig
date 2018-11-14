def setup():
    global viewport;
    size(500,400,P3D);
    viewport=createGraphics(400,200);
def draw():
    fill(15);    
    ellipse(100,100,100,100);
    fill(254,120,100);
    line(100,100,100,300);
    line(100,200,150,250);
    line(100,200,50,250);
    #line(100,300,50,250);
    line(100,300,150,350);
    line(100,300,50,350);
    #ellipse(100,300,10,10);
#print (mouseX,mouseY);
    
