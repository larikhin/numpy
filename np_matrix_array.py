import numpy as np

print('Matrix is 2d Array')
m = np.mat('1 2 3 4; 7 5 3 2; 1 2 3 4 ')
print(m)

print('\n Create main diag and matrix')
d = np.diag([1,4,5])
print(d)

print('\n Only main diagonal')
d = np.diag([[22,33,44],[55,66,77],[88,99,00]])
print(d)

d = np.diagflat([[1,2,3],[4,5,6,],[7,8,9]])
print('main diagonal\n', d)

t = np.tri(4)
print('triangle matrix\n', t)

tm = np.tril(m)
print('From array to triangle matrix\n', m,'\n', tm)
tm = np.triu(m)
print(tm)
