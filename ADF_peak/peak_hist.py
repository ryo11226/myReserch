import cv2
import numpy as np
import matplotlib.pyplot as plt
import histgram
import csv

def listed(im):#return location of peak as list
    b = im.split()
    a = [float(s) for s in b]
    im = [a[i:i+36] for i in range(0,1296,36)]
    peak = []
    for i in range(0,35):
        for j in range(0,35):
            if im[i-1][j-1]>im[i][j]:
                continue
            elif im[i-1][j]>im[i][j]:
                continue
            elif im[i-1][j+1]>im[i][j]:
                continue
            elif im[i][j-1]>im[i][j]:
                continue
            elif im[i][j+1]>im[i][j]:
                continue
            elif im[i+1][j-1]>im[i][j]:
                continue
            elif im[i+1][j]>im[i][j]:
                continue
            elif im[i+1][j+1]>im[i][j]:
                continue
            else:
                im[i][j] = 4.3e+007
                peak.append([i, j])
    im = np.array(im)
    im = np.interp(im, (im.min(), im.max()), (0, 255))
    #cv2.imwrite('ADFpeak.bmp', im)
    return peak


def peakcacher(im, peaklist):#return list of peak intensity
    intensity = []
    b = im.split()
    a = [float(s) for s in b]
    im = [a[i:i+36] for i in range(0,1296,36)]
    for i in range(0, len(peaklist)):
        if peaklist[i][0] > 5:#ADF像の上部を取り除く
            intensity.append(im[peaklist[i][0]][peaklist[i][1]])
            print(peaklist[i])
        else:
            continue
    return intensity

input = '200127\SI data (25)\ADF Image.txt'
f = open(input)
im = f.read()
f.close


c = peakcacher(im, listed(im))

firstL = [float(s)/536891.393939395 - 34.5979779444135 for s in c if s < 19400000]
secondL = [float(s)/536891.393939395 - 34.5979779444135 for s in c if s > 19400000]
histgram.doublehist(firstL, secondL, 128, 0, 3)
'''
#ここからヒストグラムの数値化
c = [float(s)/536891.393939395 - 34.5979779444135 for s in c]
hist = np.histogram(c, 50, range = (0, 5))
print(hist[0])
with open(r'200127\SI data (25)\ADF_intensity\peak_hist_x.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(hist[1])
'''