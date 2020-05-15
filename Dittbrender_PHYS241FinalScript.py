from fit_curve_array_01.py import fit_curve_array
from matplotlib.pyplot import xlabel, ylabel
from numpy import linspace
from quadratic_fit_01.py import quadratic_fit
from plot_data_with_fit_01 import plot_data_with_fit
from lowest_eigenvectors_01 import lowest_eigenvectors
from univariate_statistics_01 import univariate_statistics
from two_column_text_read_01 import two_column_text_read
from Equations_of_state.py import fit_eos
from generate_matrix.py import gm

# As discussed and shown to you in collab, it was borderline impossible to know if I was doing this right,
# My modules couldnt be found every time i typed them in so i have no idea if the numbers were going through them correctly
# i decided to make a test file to at the very lest make sure the graph things worked, by using random numbers (close to what should have been the correct ones)
# As suppose to finding mean, eigenvectors and everything else, i was just hoping that it would work if i commit and push everything but if it didn't, im unsure of what else i could have done
# Because of the immediate errors, none of my pictures/graphs will save
# Not trying to make excuses for mistakes, but i just did not have a way to test anything besides testing basic numbers
# Thank you for understanding, and have a great summer.


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
minimum_y = statistics[4]
maximum_y = statistics[5]

Eos_fit = fit_eos(data[0], data[1], quadratic_fit(data), eos='birch-murnaghan')

fit_curve = fit_curve_array(Eos_fit, minimum_x, maximum_x)
format_x = xlabel('X-axis')
format_y = ylabel('Y-axis')
graph = plot_data_with_fit(data, fit_curve, format_x, format_y)

# convert from atomic units to cubic angstoms and electonvolts

# plot data, volume on horizontal axis, energy on the vertical axis
import matplotlib.pyplot as plt
plt.plot(data[0], data[1], color='black', marker='o', markerfacecolor='blue')
plt.xlabel('E, eV/atom')
plt.ylabel('V, A^3/atom')
plt.text(80, -800, "Created by Mathew Dittbrender 2020-05-12")
plt.title("Equation of State for CU in DFT")
display_graph = True
def annotat_plot(chem_symbol, crystal_symbol, density_func):
    annotation_chem_symbol = plt.annotate(chem_symbol, xy=(210, 0.03))
    annotation_crystal = plt.annotate(crystal_symbol, xy=(230, -.04))
    annotation_density_func = plt.annotate(density_func, xy=(210, -.05))
    return (annotation_chem_symbol, annotation_crystal, annotation_density_func)

volumes = linspace(minimum_x, maximum_x, len(Eos_fit))
energy = linspace(minimum_y, maximum_y, len(Eos_fit))
volume_energy = volumes, energy

format = chem_symbol, crystal_symbol, density_func
format_list = list(format)

curve_plot = plot_data_with_fit(data, format_list, volume_energy)

if display_graph == True:
    plt.savefig("Dittbrender.Cu.png")
elif display_graph == False:
    plt.show()

# part 2
# square 130, 200
square_matrix = gm.generate_matrix(minimum_x, maximum_x,):
print(square_matrix)

eigenvalues, eigenvectors = lowest_eigenvectors(square_matrix, number_of_eigenvectors=3)
print(eigenvalues)

ndim1 = 130
parameter = 200
x = linspace(-10, 10, ndim1)

# plot

plotpoint1 = plt.plot(x, eigenvectors[0][0:ndim1])
plotpoint2 = plt.plot(x, eigenvectors[1][0:ndim1])
plotpoint3 = plt.plot(x, eigenvectors[2][0:ndim1])
display_graph = True
plt.xlabel("x[a.u]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.legend(plotpoint1, plotpoint2, plotpoint3)
plt.axis([-10, 10, max(eigenvectors[0]), - 2, max(eigenvectors[0]) + 2])
plt.axhline(color="black")
plt.text(-9, -1.6, 'created by Matt Dittbrender 2020-05-14')
plt.title("Select Wavefunctions for a Square Potential on a Spatial Grid of Points")
if display_graph == True:
    plt.savefig("Dittbrender.Square.png")
elif display_graph == False:
    plt.show()










