from matplotlib import pyplot as plt


def boxplot(x_data, x_labels, x_label, y_label, title):
    """
    """
    fig, ax = plt.subplots()

    plt.boxplot(x_data, showmeans=True, meanline=True, vert=True, labels=x_labels)

    __show_plot(fig, ax, title, xlabel=x_label, ylabel=y_label)


def __show_plot(fig, ax, title, xlabel='none', ylabel='none'):
    plt.style.use("fivethirtyeight")

    plt.title(title)
    if xlabel != 'none':
        ax.set_xlabel(xlabel)

    if ylabel != 'none':
        ax.set_ylabel(ylabel)

    # plt.yscale("log")
    # plt.autoscale(enable=True, axis='y')

    plt.tight_layout()
    # plt.savefig(output_title)

    plt.show()
