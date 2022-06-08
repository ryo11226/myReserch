import cv2
import numpy as np

# 入力画像を読み込み
img = cv2.imread("Pt1-17.jpg")

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# cv2.sobelメソッドを使用
gray_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
gray_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
dst = np.sqrt(gray_x ** 2 + gray_y ** 2)

# 結果を出力
cv2.imwrite("sobel_Pt1-17.png", dst)
