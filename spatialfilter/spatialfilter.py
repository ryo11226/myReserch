#coding: UTF-8

import numpy as np
import cv2
from PIL import Image

image = cv2.imread('Image.bmp',0)

fimage=np.fft.fft2(image)

#フーリエ変換後の行列を表示
print(fimage)
print(fimage.shape)

#中心位置を合わせる
fimage=np.fft.ffthsift(fimage)

#フィルタの作成
size = image.shape
filter_matrix = np.zeros(size)

length = size[0]
center = size[0]/2

for i in range(0,length):
     for j in range(0,length):
            d = np.sqrt((i-center)*(i-center) + (j-center)*(j-center))
            plus_gaussian = np.exp(-d ^ (2) / (2 * 10 ^ (2)))/ (np.sqrt(2 * 3.14) * 10) * 400
            minus_gaussian = -np.exp(-d ^ (2) / (2 * 8 ^ (2))) / (np.sqrt(2 * 3.14) * 8) * 300
            filter_matrix[i][j] = plus_gaussian + minus_gaussian

fimage = fimage*filter_matrix
fimage = np.fft.fftshift(fimage) #shiftする
fimage = fimage*filter_matrix
fimage = np.fft.fftshift(fimage) #shiftしたものをもとに戻す
ifimage = np.fft.ifft2(fimage) #Inverse Fourier Transform
ifimage = ifimage.real
Image.fromarray(np.uint8(ifimage)).show()
