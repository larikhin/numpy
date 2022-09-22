import numpy as np

print('\n__print data types in pandas__\n')
for k,v in np.sctypeDict.items():
    print(f'for dtype "{k}" the data type is "{v}"')


a = np.array([1,2,3,4], dtype='str_')
print(a, a.dtype)

print( '\n__converting data type__' )
print(np.complex64(10))
print(np.int0(234.324))

print('\n__unexpected results after converting__')
a = 8888
print(a,np.int8(a))
print(a, a_ar:=np.array([a], dtype='int8'))

print('\n__rigth way__')
print(a, a_ar:= np.array([a]))

print('\n__converting all array__')
m = [1,2,555,7777]
m1 = np.array(m)
m2 = np.int8(m)
m3 = np.complex64(m1)
print(m1)
print(m2, 'error converting cause wrong type')
print(m3)
