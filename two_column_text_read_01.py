def two_column_text_read(filename):
    import numpy as np
    from os import path

    if path.exists(filename):
        x = []
        y = []

        infile = open(filename, 'r')
        for line in infile:
            coords = line.split()
            x.append(float(coords[0]))
            y.append(float(coords[1]))
        infile.close()

        x, y = np.array(x), np.array(y)

        data = np.vstack((x, y))

        return data
    else:
        return print("OSError: no filename found for reading")

