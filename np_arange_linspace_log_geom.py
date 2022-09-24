import numpy as np
import matplotlib.pyplot as plt

print(' array with value from start number to finish' )
print(' np.arange(stop) ')
a = np.arange(9)
print('arange(9): ', a)
a = np.arange(3,9)
print('arange(3,9):', a)
a = np.arange(3,9, 0.3)
print(' step 0.3 !!!: ', a)

pi_const = np.pi
print(pi_const)
a = np.arange(3,9, np.pi)
print(a)

print('\narray with sinus from array')
pi_array = np.arange(0, np.pi, 0.1)
sin_array = np.sin(np.arange(0, np.pi, 0.1))
cos_array = np.cos(pi_array)
print(sin_array)
x = pi_array
y = sin_array
ycos = cos_array
plt.title("Line graph")
plt.plot(x, y, color="red")
plt.plot((np.pi+x), -y, color="red")
plt.plot(x, ycos, color="blue")
plt.plot((np.pi + x), -ycos, color="blue")
# to show plot del # in next line
#plt.show()

print('\n np.linspace(start, stop, n)')
print('      n')
print('     /|\\')
print('start___stop')

for n in range(10):
    ls = np.linspace(0,10,n)
    print(f'n={n} linspace: {ls}')

print('\n logspace(start,stop,n) = 10**start...10**value...10**stop')
print(' np.logspace(start,stop,n) decimal logarithm')
print('point on log progression')
for n in range(5):
    los = np.logspace(1,3,n)
    print(f'n={n} logspace: {los}')

print('\n geomspace(start,stop,n) geometric progression')
for n in range(5):
    los = np.geomspace(3,9,n)
    print(f'n={n} logspace: {los}')

