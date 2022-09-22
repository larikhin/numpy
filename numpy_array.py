import numpy as np

#united type of data
# (y,x)
# | y axis 0
# __ x axis 1

# numpy.array(object, dtyp='' or None)
# object = list, tuple, fn()

a = np.array([1,2,3,4])
b = np.array((1,2,3,4.0))
print(a, type(a), a.dtype)
print(b, type(b), b.dtype)
c = np.array((1,'2d',3,4.0))
print(c, type(c), c.dtype)

# access to an array element
print(c[0], c[2:])
# change element and autochange type!
c[0]=444
print(c[0],c[0].dtype,c)

#generating new array from existing element
d = c[[1,1,1,1,0,0,0]]
print(d)
# inser only if True and bool=len(array)
e = c[[True,False,True,True]]
print(e)

#reshape array
a = np.array(['a','b','c','d',
    'e','f','g','h','j'])

print(a)
b = a.reshape(3,3)# square
c = a.reshape(1,9)# _ axis x
d = a.reshape(9,1)# | axis y
print(b)
print(c)
print(d)
# acces to elemen 
print(b[1][1], ' equal ', b[1,1])
