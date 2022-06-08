#関数ファイル
import matplotlib.pyplot as plt
def hist(a, bins):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hist(a, bins=bins)
    ax.set_title('test')
    ax.set_xlabel('x')
    ax.set_ylabel('N')
    fig.show()
    plt.show()

def doublehist(a, b, bins, x_min, x_max):
    plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
    plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
    plt.rcParams['font.size'] = 14 #フォントの大きさ
    plt.rcParams['axes.linewidth'] = 1.0 # 軸の線幅edge linewidth。囲みの太さ
    plt.figure()
    plt.hist(a, bins=bins, range = (x_min, x_max), histtype='stepfilled', color='b')
    plt.hist(b, bins=bins, range = (x_min, x_max), alpha=1, histtype='stepfilled', color='b')
    plt.xlabel("Normalized Peak Intensity (a.u.)")
    plt.ylabel("Frequency")
    #plt.show()
    plt.savefig('200127\SI data (25)\ADF_intensity\Peak_hist_4.pdf')