import cv2
import numpy as np

def listed(impath):
    im = cv2.imread(impath, 0)
    height = im.shape[0]
    width = im.shape[1]
    im = im.tolist()
    print(im)
    for i in range(0, height-1):
        for j in range(0, width-1):
            if im[i-1][j-1]<im[i][j]:
                continue
            elif im[i-1][j]<im[i][j]:
                continue
            elif im[i-1][j+1]<im[i][j]:
                continue
            elif im[i][j-1]<im[i][j]:
                continue
            elif im[i][j+1]<im[i][j]:
                continue
            elif im[i+1][j-1]<im[i][j]:
                continue
            elif im[i+1][j]<im[i][j]:
                continue
            elif im[i+1][j+1]<im[i][j]:
                continue
            else:
                im[i][j] = 0
    im = np.array(im)
    cv2.imwrite(impath[:-4] + "_rpeak.bmp", im)

impath = "ADF Image.bmp"
listed(impath)
