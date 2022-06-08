import numpy as np
import cv2
from PIL import Image

#パラメータ
s = 10 #s1
r = 8 #s2
a = 400 #a
b = 300 #b
x = 0.49 #逆空間のピクセルサイズ

image = cv2.imread('SI8.bmp',0)
fimage=np.fft.fft2(image)#FFT

#フーリエ変換後の行列を表示
print(fimage)
print(fimage.shape)

#中心位置を合わせる
fimage=np.fft.fftshift(fimage)
mag = 20*np.log(np.abs(fimage))
cv2.imwrite("FFT of 8.bmp", mag)
#フィルタの作成
size = image.shape
filter_matrix = np.zeros(size)
height,width = size[:2]#これ大丈夫？
center = size[0]/2

for i in range(0,height):
     for j in range(0,width):
            d = np.sqrt((i-center)*(i-center) + (j-center)*(j-center))* 16 * x / 8.13
            plus_gaussian = np.exp(-d *d / (2 * s *s))/ (np.sqrt(2 * 3.14) * s) * a
            minus_gaussian = np.exp(-d *d / (2 * r *r)) / (np.sqrt(2 * 3.14) * r) * b * (-1)
            filter_matrix[i][j] = plus_gaussian + minus_gaussian

print(filter_matrix)

#フィルタの適用
fimage = fimage*filter_matrix
fimage = np.fft.fftshift(fimage) #shiftしたものをもとに戻す
ifimage = np.fft.ifft2(fimage) #IFFT
ifimage = ifimage.real
ifimage = ifimage *0.7
Image.fromarray(np.uint8(ifimage)).show()
cv2.imwrite("filtered_SI8.bmp",ifimage)

filter_matrix = filter_matrix*60
cv2.imwrite("filter_matrixSI8.bmp",filter_matrix)
