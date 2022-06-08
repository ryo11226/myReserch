import numpy as np
import matplotlib.pyplot as plt
import cv2

# 初期条件
input_file_name = "Smoothed_Pt1-17.txt"
devide_border = np.array([1477340, 1764380, 2055300, 3934049])

# ファイルのロードb
input_data = np.loadtxt(input_file_name)

# color
color = np.array([[0, 0, 253],
                  [1, 127, 1],
                  [1, 255, 0],
                  [123, 0, 0],
                  [255, 255, 255],
                  [162, 2, 125],
                  [255, 0, 255],
                  [0, 0, 0]])
color_blue = color[:, 0]
color_green = color[:, 1]
color_red = color[:, 2]


def blue_func(intensity, devide_border):
    for i in range(devide_border.shape[0]):
        if intensity < devide_border[i]:
            return color_blue[i]
    return color_blue[devide_border.shape[0]]

def green_func(intensity, devide_border):
    for i in range(devide_border.shape[0]):
        if intensity < devide_border[i]:
            return color_green[i]
    return color_green[devide_border.shape[0]]


def red_func(intensity, devide_border):
    for i in range(devide_border.shape[0]):
        if intensity < devide_border[i]:
            return color_red[i]
    return color_red[devide_border.shape[0]]


blue_data = np.array([[blue_func(input_data[j, i], devide_border)
                       for i in range(input_data.shape[0])] for j in range(input_data.shape[0])])
green_data = np.array([[green_func(input_data[j, i], devide_border)
                        for i in range(input_data.shape[0])] for j in range(input_data.shape[0])])
red_data = np.array([[red_func(input_data[j, i], devide_border)
                      for i in range(input_data.shape[0])] for j in range(input_data.shape[0])])
color_data = np.dstack([blue_data, green_data, red_data])

color_data_name = input_file_name[:-4]
for border_name in devide_border:
    color_data_name += "_" + str(border_name)

cv2.imwrite(color_data_name + ".png", color_data)
