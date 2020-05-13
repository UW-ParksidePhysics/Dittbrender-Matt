print('%12s %12s' %('Fahrenheit', 'Celcius'))
print('---------------------')
infile = open('f2c_data2.txt', 'r')
infile.readline()
infile.readline()
infile.readline()

for line in infile:
    F = float(line.split()[2])
    C = (5.0/9)*(F-32)
    print('%12.4f %12.4f' %(F, C))
