import numpy as np

A = np.array([-2, -2])
B = np.array([1, 3])
C = np.array([4, -1])

def dir_vec(AB):
	return np.matmul(AB, dvec)

def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))

dvec = np.array([-1, 1])
omat = np.array([[0, 1], [-1, 0]])

AB = np.vstack((A, B)).T
BC = np.vstack((B, C)).T
CA = np.vstack((C, A)).T

eq_AB = np.append(norm_vec(AB), -np.matmul(norm_vec(AB), A))
eq_BC = np.append(norm_vec(BC), -np.matmul(norm_vec(BC), B))
eq_CA = np.append(norm_vec(CA), -np.matmul(norm_vec(CA), C))

eq_AP = np.append(dir_vec(BC), -np.matmul(dir_vec(BC), A))
eq_BQ = np.append(dir_vec(CA), -np.matmul(dir_vec(CA), B))
eq_CR = np.append(dir_vec(AB), -np.matmul(dir_vec(AB), C))
print(eq_AP)
print(eq_BQ)
print(eq_CR)