import numpy as np
import matplotlib.pyplot as plt
import cv2

# 初期設定
input_file_name = "Smoothed_Pt1-17.txt"
dispersion_size = 9
input_rate =0.3

# データをロード
input_data = np.loadtxt(input_file_name)


# mirrorデータを作成
def mirror_func(position, mask_size, input_data_size):
    if position < (mask_size - 1) / 2:
        return int((mask_size - 1) / 2 - position)
    elif (mask_size - 1) / 2 <= position < (mask_size - 1) / 2 + input_data_size:
        return int(position - (mask_size - 1) / 2)
    elif position >= (mask_size - 1) / 2 + input_data_size:
        return int(2 * input_data_size - position + (mask_size - 1) / 2 - 2)
    else:
        print("there is a probrem!")


def make_mirror(input_data, mask_size):
    input_data_size = input_data.shape[0]
    mirror_size = input_data.shape[0] + mask_size - 1
    mirror_data = np.array(
        [[input_data[mirror_func(j, mask_size, input_data_size), mirror_func(i, mask_size, input_data_size)]
          for i in range(mirror_size)]
         for j in range(mirror_size)])
    return mirror_data


mirror_data = make_mirror(input_data, dispersion_size)


#分散データの作成
from operator import itemgetter
input_data_size = input_data.shape[0]
dispersion_data=np.array([[np.std(mirror_data[j:j+dispersion_size,i:i+dispersion_size])
                          for i in range(input_data_size)] for j in range(input_data_size)])
#np.savetxt("test.txt", dispersion_data)
list_input_data =input_data.reshape(-1,1)
list_dispersion_data=dispersion_data.reshape(-1,1)
sort_data=np.hstack([list_input_data,list_dispersion_data]).tolist()

sort_data.sort(key=itemgetter(1))
sort_data_name=input_file_name[:-4] + "_" + str(dispersion_size) + "_sort.txt"
np.savetxt(sort_data_name,sort_data)