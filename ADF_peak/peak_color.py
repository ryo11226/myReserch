import cv2
import numpy as np
import matplotlib.pyplot as plt
import histgram

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
        intensity.append(im[peaklist[i][0]][peaklist[i][1]])
    return intensity

def peak_color(im, peaklist):
    b = im.split()
    b = [float(s)/536891.393939395 - 34.5979779444135 for s in b ]
    for i in range(0, 1296):
        if b[i] > 6:
            b[i] = 6
        else:
            continue
    im = [b[i:i+36] for i in range(0,1296,36)]
    for i in range(0, 36):
        for j in range(0, 36):
            if [i, j] in peaklist:
                continue
            else:
                im[i][j] = 0
    im = [im[i] for i in range(6,36)]
    return im



input = '200127\SI data (25)\ADF Image.txt'
f = open(input)
im = f.read()
f.close

peak_2ndlayer = peak_color(im, listed(im))
plt.imshow(peak_2ndlayer, cmap='Paired')
plt.colorbar () # カラーバーの表示 
'''
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
'''
plt.show()


#b = im.split()
#a = [float(s) for s in b]
#histgram.doublehist(peakcacher(im, listed(im)), a, 60, 18831288, 20000000)
