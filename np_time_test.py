import numpy as np
import time


t1 = time.time() 
a1 = np.arange(60000000)
t2 = time.time()
print (delta_1 := t2 - t1)

t1 = time.time() 
a2 = []
for value in range(60000000):
    a2.append(value)
t2 = time.time()
print (delta_2 := t2 - t1)
print (total_delta :=delta_2 - delta_1)

