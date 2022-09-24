import numpy as np

a = np.array([[1,2],[3,4]])
b = np.copy(a)

print(f'{a} \n\n {b}')
print('change b[0][0]')
b[0][0]=7
print(f'{a} \n\n {b}')

for x in b:
    print(type(x))
    print('x:',x)
for x,y in b:
    print(type(x), type(y))
    print('x:',x, 'y:',y)
