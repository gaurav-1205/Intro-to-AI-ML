import numpy as np
def mid_pt(B,C):
	D = (B+C)/2.0
	return D

def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))


def line_intersect(AD, CF):
	n1 = norm_vec(AD)
	n2 = norm_vec(CF)
	# print(n1.shape, n2.shape)
	N = np.vstack((n1, n2))
	p = np.zeros(2)
	print(AD, CF)
	p[0] = np.matmul(n1, AD[:, 0])
	p[1] = np.matmul(n2, CF[:, 0])
	return np.matmul(np.linalg.inv(N), p)

A = np.array([-2, -2])
B = np.array([1, 3])
C = np.array([4, -1])


D = mid_pt(B, C)
F = mid_pt(A, B)

AD = np.vstack((A, D)).T
CF = np.vstack((C, F)).T

dvec = np.array([-1, 1])
omat = np.array([[0, 1], [-1, 0]])

print(line_intersect(AD, CF))
#line_intersect(AD, CF)