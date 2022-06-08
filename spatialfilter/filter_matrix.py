#coding: UTF-8

import numpy as np
import cv2
from PIL import Image

#パラメータ
s = 10 #s1
r = 8 #s2
a = 400 #a
b = 300 #b
x = 0.072 #逆空間のピクセルサイズ


#フィルタの作成
filter_matrix = np.zeros((512,512))
center = 256

for i in range(0,511):
     for j in range(0,511):
            d = np.sqrt((i-center)*(i-center) + (j-center)*(j-center))* 16 * x / 8.13
            plus_gaussian = np.exp(-d *d / (2 * s *s))/ (np.sqrt(2 * 3.14) * s) * a
            minus_gaussian = np.exp(-d *d / (2 * r *r)) / (np.sqrt(2 * 3.14) * r) * b * (-1)
            filter_matrix[i][j] = plus_gaussian + minus_gaussian

filter_matrix = filter_matrix*60
print(filter_matrix)
cv2.imwrite("filter_matrix512.bmp",filter_matrix)
