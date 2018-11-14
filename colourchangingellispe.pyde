def setup():
    size(1080,1000,P3D);
    background(255)
def click():
    if(mousePressed):
        
        noStroke()
        # background(255)
        fill(255)
        ellipse(mouseX,mouseY,100,100)
def draw():
   translate(mouseX,mouseY)
   fill(mouseX%255,mouseY%255,mouseX*mouseY%255)
   noStroke()
   ellipse(mouseX,mouseY,100,100)
   click();
   
   
   
        
   
