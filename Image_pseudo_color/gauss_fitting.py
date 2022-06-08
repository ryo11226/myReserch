import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fftn
from numpy.fft import ifftn
import cv2

# 初期設定
sigma = 0.01
input_file_name = "16122_512.txt"

# 入力データをフーリエ変換し、波数空間像にする。
input_data = np.loadtxt(input_file_name)
fftn_data = fftn(input_data)
# 四隅に中心が配置されるので、中心にシフトさせる
fftn_data = np.roll(fftn_data, [(fftn_data.shape[0] - 1) // 2, (fftn_data.shape[0] - 1) // 2], axis=(0, 1))

# ガウシアンフィルタをかける
center = (fftn_data.shape[0] - 1) // 2
expx = np.array([np.exp(-(x - center) ** 2 / 2 * sigma ** 2) for x in range(fftn_data.shape[0])]).reshape(-1, 1)
expy = np.array([np.exp(-(x - center) ** 2 / 2 * sigma ** 2) for x in range(fftn_data.shape[0])]).reshape(1, -1)
conv_data = expx * fftn_data * expy
# 逆フーリエ変換する
ifftn_data = ifftn(conv_data)
ifftn_data = np.sqrt(ifftn_data.real ** 2 + ifftn_data.imag ** 2)
out_file_name = input_file_name[:-4] + "_" + str(sigma) + "_gaussian.txt"
np.savetxt(out_file_name, ifftn_data)

# 画像作成
gray_image = (ifftn_data - ifftn_data.min()) / (ifftn_data.max() - ifftn_data.min()) * 255
gray_image_name = out_file_name[:-4] + ".jpg"
cv2.imwrite(gray_image_name, gray_image)
# cv2.imshow("gray", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ガウシアンフィルタを描写
tmp = np.ones((input_data.shape[0], input_data.shape[0]))
gauss_filter = expx * tmp * expy
gauss_filter_name = str(sigma) + "_GaussFilter.txt"
np.savetxt(gauss_filter_name, gauss_filter)
