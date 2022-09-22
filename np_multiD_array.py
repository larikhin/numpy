import numpy as np

print('    Y |')
print('      |__ X')
print('__2d__  (Y,X)')
two_d_array = np.array([[1,2],[1,4],[2,3]])
print(two_d_array)
print('Y = 0 \n', two_d_array[0])
print('Y = 0, X = 0\n', two_d_array[0,0])


print()
print('    Y |')
print('      |__ X')
print('   Z /')
print('___3d (Z,Y,X)___')
tree_dimension_array = np.array([[[1,2],[3,4]],[[2,2],[3,4]],[[3,1],[3,4]]])
print(tree_dimension_array)
print('Z = 0 \n', tree_dimension_array[0])
print('Z = 0, Y = 0\n', tree_dimension_array[0,0])
print('Z = 0, Y = 0, X = 0\n', tree_dimension_array[0,0,0])

print(type(u:=tree_dimension_array[0,0,0]))
u = int(u)
print(u, type(u))
