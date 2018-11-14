int numFrames = 12;
int currentFrame = 0;
PImage[] images = new PImage[numFrames];
    
void setup() {
  size(640, 360);
  frameRate(24);
  
  images[0]  = loadImage("C:\Users\manas\Desktop");
  images[1]  = loadImage("C:\Users\manas\Desktop"); 
  images[2]  = loadImage("C:\Users\manas\Desktop");
  images[3]  = loadImage("C:\Users\manas\Desktop"); 
  images[4]  = loadImage("C:\Users\manas\Desktop");
  images[5]  = loadImage("C:\Users\manas\Desktop"); 
  images[6]  = loadImage("C:\Users\manas\Desktop");
  images[7]  = loadImage("C:\Users\manas\Desktop"); 
  images[8]  = loadImage("C:\Users\manas\Desktop");
  images[9]  = loadImage("C:\Users\manas\Desktop"); 
  images[10] = loadImage("C:\Users\manas\Desktop");
  images[11] = loadImage("C:\Users\manas\Desktop"); 
  
  
  for (int i = 0; i < numFrames; i++)
   {
    String imageName = "PT_anim" + nf(i, 4) + ".gif";
    images[i] = loadImage(imageName);
   }
} 
 
void draw() { 
  background(0);
  currentFrame = (currentFrame+1) % numFrames;  // Use % to cycle through frames
  int offset = 0;
  for (int x = -100; x < width; x += images[0].width) { 
    image(images[(currentFrame+offset) % numFrames], x, -20);
    offset+=2;
    image(images[(currentFrame+offset) % numFrames], x, height/2);
    offset+=2;
  }
}
    
