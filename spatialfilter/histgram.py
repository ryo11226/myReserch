#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    # 入力画像を読み込み
    img = cv2.imread("SI Data(40).bmp")


    # 方法1(NumPyでヒストグラムの算出)
    hist, bins = np.histogram(img.ravel(),256,[0,256])

    # 方法2(OpenCVでヒストグラムの算出)
    #hist = cv2.calcHist([img],[0],None,[256],[0,256])

    # ヒストグラムの中身表示
    print(hist)



    # グラフの作成
    plt.xlim(0, 256)
    plt.plot(hist)
    plt.xlabel("Pixel value", fontsize=20)
    plt.ylabel("Number of pixels", fontsize=20)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
