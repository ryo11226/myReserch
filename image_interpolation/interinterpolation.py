import cv2
import numpy as np

img = cv2.imread("interpolatedADF.bmp",0)

size = (img.shape)
height,width = size[:2]
print(height)

I = np.zeros((140,144))

for x in range(0,67):
    for y in range(0,69):
        I[2*x,2*y]=img[x,y]
        I[2*x+1,2*y+1]=img[x,y]/4+img[x+1,y]/4+img[x,y+1]/4+img[x+1,y+1]/4
        I[2*x+1,2*y]=img[x,y]/2+img[x+1,y]/2
        I[2*x,2*y+1]=img[x,y]/2+img[x,y+1]/2

cv2.imwrite("interinterpolatedADF.bmp",I)
