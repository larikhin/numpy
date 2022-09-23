import numpy as np

# random list of elements
a = np.empty(10)
print(a)

print('\n list of random elements direct type\n')
a = np.empty(10 , dtype = 'int8')
b = np.empty(10, dtype = 'int16')
print(' a ', a, '\n b ', b)

print('\n main diagonal with 1 on matrix\n')
e = np.eye(4)
print(e)

print('\n Square matrix \n')
s = np.identity(5)
print(s)

print('\n Zero matrix \n')
z1d = np.zeros((2))
z2d = np.zeros((3,2))
z3d = np.zeros((5,3,2))
print('1d\n', z1d)
print('2d\n', z2d)
print('3d\n', z3d)

print('\n Marix with "1" ones\n')
o = np.ones([2,6], dtype='int8')
print(o)

print('\n Matrix with direct value \n')
val = 55
f = np.full((2,4), val)

print(f)
