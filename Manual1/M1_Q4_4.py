#Find angle bisector co-ordinates on the opposite side
import numpy as np

A = np.array([-2, -2])
B = np.array([1, 3])
C = np.array([4, -1])

len_AB = np.linalg.norm(A-B)
len_BC = np.linalg.norm(B-C)
len_CA = np.linalg.norm(C-A)


U = (len_AB*C + len_CA*B)/(len_AB+len_CA)
V = (len_BC*A + len_AB*C)/(len_BC+len_AB)
W = (len_BC*A + len_CA*B)/(len_BC+len_CA)


print(U)
print(V)
print(W)
