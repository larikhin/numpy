import numpy as np


a = np.arange(0.1, 1, 0.1)
print(a)

print(f'\n array.dtype {a.dtype} size {a.size} item size byte {a.itemsize}')
print(f' array size = size * item size = {a.size*a.itemsize}')

a.dtype = np.int8()
print(f'\n array.dtype {a.dtype} size {a.size} item size {a.itemsize}')
print(f' array size = size * item size = {a.size*a.itemsize}')

a.dtype = np.float64()
print(f'\n array.dtype {a.dtype} size {a.size} item size {a.itemsize}')
print(f' array size = size * item size = {a.size*a.itemsize}')

b = np.ones((3,4,5))
print(b)

print(f'count of axes b.ndim = {b.ndim}, b.shape of array = {b.shape}\n')
b.shape = 60
print(f' reshape b.shape = new shape b.shape = 3*4*5\n{b}')
print(b.shape)

b.shape = 5,12
print(b)

print(f'\n linking and reshaping b,  c = b.reshape(2,3,10)')
print('the array is the SAME')
c = b.reshape(2,3,10)
print(c)

b[0,0]= 100
print(c)
print(f'but id is different id b={id(b)} id c={id(c)}')

print(' "-1" means that it will autocalculate ')
z = b.reshape(2,3,-1)
print('(2,3,-1)\n',z)
z = b.reshape(-1,1)
print('(-1,1)\n',z)
z = b.reshape(1,-1)
print('(1,-1)\n', z)


# if ([value]) - vector
# if ([[value]]) - matrix
