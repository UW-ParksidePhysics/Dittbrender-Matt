from fit_curve_array_01.py import fit_curve_array
from matplotlib.pyplot import xlabel, ylabel
from quadratic_fit_01.py import quadratic_fit
from plot_data_with_fit_01 import plot_data_with_fit
from lowest_eigenvectors_01 import lowest_eigenvectors
from univariate_statistics_01 import univariate_statistics
from two_column_text_read_01 import two_column_text_read
from Equations_of_state.py import fit_eos




def parse_file(filename):
    axis_names = filename.split('.')
    chem_symbol = axis_names[0]
    crystal_symbol = axis_names[1]
    density_func = axis_names[2]
    return chem_symbol, crystal_symbol, density_func


filename = 'Cu.Fm-3m.GGA-PBE.volumes_energies.dat'
data = two_column_text_read(filename)

statistics = univariate_statistics(data)
mean = statistics[0]
standard_deviation = statistics[1]
minimum_x = statistics[2]
maximum_x = statistics[3]

Eos_fit = fit_eos(data[0], data[1], quadratic_fit(data), eos='birch-murnaghan')

fit_curve = fit_curve_array(Eos_fit, minimum_x, maximum_x)
format_x = xlabel('X-axis')
format_y = ylabel('Y-axis')
graph = plot_data_with_fit(data, fit_curve, format_x, format_y)

# convert from atomic units to cubic angstoms and electonvolts

# plot data, volume on horizontal axis, energy on the vertical axis
import matplotlib as plt
plt.plot(data[0], data[1], color='black', marker='o', markerfacecolor='blue')
plt.xlabel('E, eV/atom')
plt.ylabel('V, A^3/atom')

def annotate_graph():




