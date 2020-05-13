def convert_units(data):
    volume_conversion = data[0] * (5.29 * (10 ** -11))
    energy_conversion = data[1] * (5.29 * (10 ** -11))
    bulkus_module = energy_conversion / volume_conversion
    return volume_conversion, energy_conversion, bulkus_module

    #The bulkus module looks to include pressure, which im not sure how to find
