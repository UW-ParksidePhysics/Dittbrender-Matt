import sys
<<<<<<< HEAD
try:
    F = float(input(sys.argv[1]))
except IndexError:
    print('Temp only in Celsius')
    sys.exit(1)

C = 5/9 * (F - 32)
print("%g Fahrenheit - %g Celsius" % (F, C))
=======

try:
    F=float(sys.argv[1])
    C=(5.0/9)*(F-32)
    print (C)
except IndexError:
    raise IndexError('I think you are forgetting something')
>>>>>>> origin/master
