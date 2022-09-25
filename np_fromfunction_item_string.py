import numpy as np


def f_x(y,x):
    return x 
def f_y(y,x):
    return y

def f_xy(y,x):
    return y,x


print('exucute function for each coordinate')
a = np.fromfunction(f_x, (2,2))
print(a)
a = np.fromfunction(f_y,(2,2))
print(a)
a = np.fromfunction(f_xy,(10,10))
print(a)

a = np.fromfunction(lambda x, y:x+y, (2,2))
print('lambda a:', a)

print('\n From iter')
print(i := np.fromiter('fasfd asdfa', dtype='<U1'))

print('\n From iter function with yield')
def getRange(n):
    i=0
    for item in range(n):
        i+=1
        yield item + i

y = np.fromiter(getRange(5), dtype='int8')
print(y)

print('\n From string')
print(s:=np.fromstring('123,3,33', sep = ','))
