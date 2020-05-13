import sys
try:
    F = float(input(sys.argv[1]))
except IndexError:
    print('Temp only in Celsius')
    sys.exit(1)

C = 5/9 * (F - 32)
print("%g Fahrenheit - %g Celsius" % (F, C))
