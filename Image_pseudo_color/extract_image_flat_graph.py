import numpy as np
import matplotlib.pyplot as plt


#初期設定
input_file_name="Smoothed_Pt1-17_9_sort.txt"
input_rate=0.2
bins_size=200

input_data=np.loadtxt(input_file_name)
input_num=int(input_data.shape[0]*input_rate)

rate_input_data=input_data[0:input_num,:]

n, bins, patches= plt.hist(rate_input_data[:,0],bins=bins_size)
n=np.hstack([n,0])
array_n=np.array(n).reshape(-1,1)
array_bins=np.array(bins).reshape(-1,1)

hist_info = np.hstack([array_bins,array_n])
graph_name=input_file_name[:-4]+"_" + str(input_rate) +"_rate.txt"
np.savetxt(graph_name,hist_info)

plt.yscale("log")
plt.grid(True)
image_name=input_file_name[:-4]+"_" + str(input_rate) +"_rate.png"
plt.savefig(image_name)
plt.show()
