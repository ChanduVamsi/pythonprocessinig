
def setup():
    size(800,800,P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)
    background(255)
    
def draw():
    pushMatrix()
    
    noStroke()
    translate(180,250)
    background(0)
    #sphere(300)
    popMatrix()


def draw():
    global time






    background (0, 250, 0)
    camera (0, 0, 70, 0, 0, 0, 0,  1, 0)

    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    directionalLight (100, 100, 100, -0.3, 0.5, 1)
    
    noStroke()
    shininess(20)

    pushMatrix()
    Model()
    popMatrix()
    

def Model():
    head()
    body()
    arms()
    nose()
    eyes()
    smile()



def nose():
    #nose
    fill(255, 0, 0)
    pushMatrix()
    translate(0, -3, 13.9)
    rotateZ(radians(180))
    scale(.6, .2, .1)
    #triangularPrism()
    popMatrix()

def body():
    #body
    fill(255,255,255)
    pushMatrix()
    translate(0, 0, 0)
    scale(2.3, 4.3, 2)
    sphere(60)
    sphere(5)
    popMatrix()

def arms():
    #right arm
    fill(255, 255, 255)
    pushMatrix()
    translate(10, 5, 6)
    rotateY(radians(-75))
    rotateZ(radians(55))
    scale(2.0, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()

    #left arm
    pushMatrix()
    translate(-10, 5, 6)
    rotateY(radians(75))
    rotateZ(radians(-55))
    scale(2.0, .5, .5)
    sphereDetail(80)
    sphere(5)
    popMatrix()

def head():
    #head
    fill(255, 255, 255)
    pushMatrix()
    translate(0, -8, 0)
    scale(2.3, 2.6, 3)
    sphere(60)
    sphere(5)
    popMatrix()



def eyes():
    #left eye
    fill(0, 255, 0)
    pushMatrix()
    translate(-4, -6, 12.2)
    scale(.5, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()

    #right eye
    fill(0, 255, 0)
    pushMatrix()
    translate(4, -6, 12.2)
    scale(.5, .5, .5)
    sphereDetail(60)
    sphere(5)
    popMatrix()


def smile():
    pushMatrix()
    stroke(0, 0, 0)
    translate(0, -2, 13.4)
    scale(.4, .4, .4)
    rotateX(radians(-30))
    curve(-10, -2, -6, 5, 0, 0, 0, 0)
    curve(0, 0, 0, 0, 6, 5, 10, -2)
    popMatrix()
           
       
