def setup():
    size(800,600,P3D);
    background(0)
def draw():
    pushMatrix()
    translate(400,300)
    rotate(mouseX);
    #lights()
    fill(245,125,0)
    #stroke(204,102,10)
    sphere(100)
    popMatrix()
    
        
    
