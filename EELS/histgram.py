import matplotlib.pyplot as plt
def hist(a, bins):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hist(a, bins=bins)
    ax.set_xlabel('ADF Intensity (a.u.)')
    ax.set_ylabel('Frequency')
    fig.show()
    plt.show()

def doublehist(a, b, bins, x_min, x_max):
    plt.figure()
    plt.hist(a, bins=bins, range = (x_min, x_max), histtype='stepfilled', color='b')
    plt.hist(b, bins=bins, range = (x_min, x_max), alpha=1, histtype='stepfilled', color='g')
    plt.xlabel("ADF Intensity (a.u.)")
    plt.ylabel("Frequency")
    plt.show()


def quadhist(a, b, c, d, bins, x_min, x_max):
    plt.figure()
    plt.hist(a, bins=bins, range = (x_min, x_max), histtype='stepfilled', color='b')
    plt.hist(b, bins=bins, range = (x_min, x_max), alpha=1, histtype='stepfilled', color='g')
    plt.hist(c, bins=bins, range = (x_min, x_max), histtype='stepfilled', color='r')
    plt.hist(d, bins=bins, range = (x_min, x_max), alpha=1, histtype='stepfilled', color='y')
    plt.xlabel("ADF Intensity (a.u.)")
    plt.ylabel("Frequency")
    plt.show()