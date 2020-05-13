def plot_data_with_fit(fit_curve, data, fit_format, format_y=None, format_x=None):
    import matplotlib.pyplot as plt
    plt.title('Final Curve Plot')
    format_x
    format_y

    plt.scatter(data[0], data[1], label = 'Data', s=1)
    plt.plot(fit_curve[0], fit_curve[1], 'r')
    plt.show()
    return


