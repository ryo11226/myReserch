import matplotlib.pyplot as plt
import numpy as np

def meaner(data):
    mean = sum(data)/len(data)
    return mean

def data_energy(input, einit, ebin):
    f = open(input)
    num = f.read()
    f.close
    a = num.split()
    data = [float(s) for s in a ]
    energy = [einit + ebin * i for i in range(0, 2046)]
    return data, energy, max(data), min(data)

def trimer(data, energy, emin, emax, einit, ebin):
    i_min = int((emin - einit)/ebin)
    i_max = int((emax - einit)/ebin)
    x_axis = energy[i_min:i_max]#＋１してもいいかも
    y_axis = data[i_min:i_max]
    y_axis = [2*(s-min(y_axis))/(max(y_axis) - min(y_axis)) -1 for s in y_axis]#nomalization
    return x_axis, y_axis, max(y_axis)

def plotter(dataset1, dataset2, dataset3):
    plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
    plt.rcParams['font.size'] = 14 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.0 # 軸の線幅edge linewidth。囲みの太さ
    plt.rcParams['xtick.direction'] = 'in'
    plt.xlabel("Energy Loss [eV]")
    plt.ylabel("Intensity (a. u.)")
    ax = plt.gca()
    ax.axes.yaxis.set_ticks([])
    ax.set_ylim(-1, 4)
    #plt.plot(dataset3[0], list(map(lambda x: x*0.8*2, dataset3[1])), color = "gray", linewidth = 1.5)
    plt.plot(dataset2[0], list(map(lambda x: x*0.4+dataset3[2]*2, dataset2[1])), color = "blue", linewidth = 1.5)
    plt.plot(dataset1[0], list(map(lambda x: x+dataset2[2]*2, dataset1[1])), color = "red", linewidth = 1.5)
    plt.show()
    #plt.savefig("nitrogen.png")


e_min = 390
e_max = 430

c_pi = 287.62
e_dif = c_pi - 285
e_init = 52.42
e_init = e_init - e_dif

nitro1 = data_energy(r'200127\SI data (5)\N_spe\2_edge.txt', e_init, 0.4)
nitrogen1 = trimer(nitro1[0], nitro1[1], e_min, e_max, e_init, 0.4)

nitro2 = data_energy(r'200127\SI data (5)\N_spe\1st layer_edge.txt', e_init, 0.4)
nitrogen2 = trimer(nitro2[0], nitro2[1], e_min, e_max, e_init, 0.4)


plotter(nitrogen1, nitrogen2, [0, 0, 0])