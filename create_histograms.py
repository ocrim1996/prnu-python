from matplotlib import pyplot as plt


def create_histogram_plot(y_value, labels_value, device_name):
    x = [i for i in range(20)]
    labels = labels_value
    y = y_value

    plt.bar(x, height=y)
    plt.xticks(x, labels, rotation='vertical')

    # Pad margins so that markers don't get
    # clipped by the axes
    plt.margins(0.1)

    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.5)

    plt.xlabel("Image tested", labelpad=7)
    plt.ylabel("PCE", labelpad=7)

    plt.title("PCE of " + str(device_name) + " with DRUNet")
    outpath = "/Users/mircoceccarelli/PyCharmProjects/prnu-python/Histograms_with_DRUNet/"
    plot_name = outpath + "PCE_of_" + str(device_name)+".png"

    plt.savefig(plot_name)
    plt.show()
