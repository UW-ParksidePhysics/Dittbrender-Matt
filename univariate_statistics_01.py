def univariate_statistics(data):
    from math import sqrt

    if not len(data) == 2:
        print("IndexError: not two rows")
    elif (len(data[0]) or len(data[1])) <= 1:  # elif is another if statement within an if statement
        print("IndexError: not more than one column")
    else:
        minimum_x_value = min(data[0])
        maximum_x_value = max(data[0])
        minimum_y_value = min(data[1])
        maximum_y_value = max(data[1])

        # finding the mean (for just y values)
        mean = sum(data[1])/len(data[1])
        print("The mean is:", mean)

        # Finding Standard Deviation (for just y values)
        data_standard = data
        Sum_standard = sqrt(sum(data_standard[0]) ** 2 + sum(data_standard[1]) ** 2)
        Len_standard = sqrt(len(data_standard[0]) ** 2 + len(data_standard[1]) ** 2)
        standard_deviation = sqrt(Sum_standard / Len_standard)
        print("The standard deviation is:", standard_deviation)



