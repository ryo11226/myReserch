import numpy as np
import matplotlib.pyplot as plt
import cv2
import histgram
import csv

input = r"200127\SI data (25)\C_map\Signal (280 - 330 eV) from EELS Spectrum Image (high-loss) (aligned).txt"
f = open(input)
num = f.read()
f.close
a = num.split()
b = [float(s) for s in a ]
im = b[36:1296]


histgram.hist(im, 80)


#ここからヒストグラムの数値化
im = [s for s in im if s < 80000]

hist = np.histogram(im, 80, range = (0, 80000))
print(hist[0])
with open(r'200127\SI data (25)\C_map\C_map_hist_x.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(hist[1])