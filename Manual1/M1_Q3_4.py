import numpy as np

A = np.array([-2, -2])
B = np.array([1, 3])
C = np.array([4, -1])

def dir_vec(AB):
	return np.matmul(AB, dvec)

def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))

def line_intersect(n1, CF, p0):
	n2 = norm_vec(CF)
	# print(n1.shape, n2.shape)
	N = np.vstack((n1, n2))
	p = np.zeros(2)
	p[0] = p0
	p[1] = np.matmul(n2, CF[:, 0])
	return np.matmul(np.linalg.inv(N), p)

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

P = line_intersect(dir_vec(BC), BC, np.matmul(dir_vec(BC), A))
Q = line_intersect(dir_vec(CA), CA, np.matmul(dir_vec(CA), B))
R = line_intersect(dir_vec(AB), AB, np.matmul(dir_vec(AB), C))

AP = np.vstack((A, P)).T
BQ = np.vstack((B, Q)).T
CR = np.vstack((C, R)).T

H = line_intersect(dir_vec(CA), AP, np.matmul(dir_vec(CA), B))

print("HA : ",np.linalg.norm(H-A))

print(P)
print(Q)
print(R)

print(H)