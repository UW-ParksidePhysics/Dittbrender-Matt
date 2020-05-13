def fit_curve_array(data, quadratic_coefficients, minimum_x, maximum_x, number_of_points):
    import numpy as np
    number_of_points = data[0] * data[1]
    if maximum_x < minimum_x:
        print("Arithmetic Error")

    if number_of_points <= 2:
        print("Index Error")

    else:
        x = np.linspace(minimum_x, maximum_x, number_of_points)
        y = np.polyval(quadratic_coefficients, x)
        fit_curve = np.vstack(x, y)
        return fit_curve



