from numpy import sort
from numpy.linalg import linalg
from numpy.ma import zeros


def lowest_eigenvectors(square_matrix, number_of_eigenvectors):
    Mrows = len(square_matrix)
    count = 0
    while count < Mrows:
        Mcolumns = len(square_matrix[count])
        if not Mrows == Mcolumns:
            return print("must be a square matrix")


number_of_eigenvectors = 3

A = zeros([10, 10])

n = 0
while n <= 9:
    A[n, n] = 2
    n = n + 1

while n<= 8:
    A[n, n + 1] = 1
    A[n + 1, n] = 1
    n = n + 1

H = (1 / (2 *(1 / 9 ** 2))) * A

(V, D) = linalg.eig(H)
order = sort(V)
print(order)

print(V[order[0:3]])
print(D[order[0:3]])

