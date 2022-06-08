import numpy as np
import cv2
import matplotlib.pyplot as plt


#2の累乗pxにしか変換できない。
#初期条件
input_file_name = "16122.txt"
new_size = 512


input_data = np.loadtxt(input_file_name)

resize_size=int(input_data.shape[0]/new_size)

output_data =np.array([[np.mean(input_data[resize_size*i:resize_size*i+resize_size,
                        resize_size*j:resize_size*j+resize_size])
                        for j in range(new_size)] for i in range(new_size)])
np.savetxt(input_file_name[:-4] + "_" + str(new_size) + ".txt", output_data)

gray_data = (output_data-output_data.min())/(output_data.max()-output_data.min())*255
cv2.imwrite(input_file_name[:-4] + "_" + str(new_size) + ".jpg", gray_data)
plt.show()
