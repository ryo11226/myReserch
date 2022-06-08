import cv2
import numpy as np

im=cv2.imread("Cmap.bmp",0)

for i in range(0,400):
    for j in range(0,400):
        a=im[i,j]

        if a<27:
            im[i,j]=0

        elif a<149:
            im[i,j]=85

        elif a<271:
            im[i,j]=170

        else:
            im[i,j]=256

print(im)
cv2.imwrite("4EELS-C.bmp",im)
