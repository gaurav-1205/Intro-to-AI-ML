import numpy as np

def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))


def line_intersect(AD, CF):
	n1 = norm_vec(AD)
	n2 = norm_vec(CF)
	# print(n1.shape, n2.shape)
	N = np.vstack((n1, n2))
	p = np.zeros(2)
	p[0] = np.matmul(n1, AD[:, 0])
	p[1] = np.matmul(n2, CF[:, 0])
	return np.matmul(np.linalg.inv(N), p)

A = np.array([-2, -2])
B = np.array([1, 3])
C = np.array([4, -1])

len_AB = np.linalg.norm(A-B)
len_BC = np.linalg.norm(B-C)
len_CA = np.linalg.norm(C-A)


U = (len_AB*C + len_CA*B)/(len_AB+len_CA)
V = (len_BC*A + len_AB*C)/(len_BC+len_AB)
W = (len_BC*A + len_CA*B)/(len_BC+len_CA)

AU = np.vstack((A, U)).T
BV = np.vstack((B, V)).T
CW = np.vstack((C, W)).T

dvec = np.array([-1, 1])
omat = np.array([[0, 1], [-1, 0]])

print(line_intersect(AU, BV))
print(line_intersect(CW, BV))

incentre = (len_BC*A+len_CA*B+len_AB*C)/(len_AB+len_BC+len_CA)
print(incentre)