import numpy as np
import matplotlib.pyplot as plt

A = np.array([-2, -2])
B = np.array([1, 3])
C = np.array([4, -1])

def dir_vec(AB):
	return np.matmul(AB, dvec)


def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))


def mid_pt(B,C):
	D = (B+C)/2.0
	return D

dvec = np.array([-1, 1])
omat = np.array([[0, 1], [-1, 0]])

D = mid_pt(B,C)
E = mid_pt(A,C)
F = mid_pt(A,B)

AD = np.vstack((A, D)).T
BE = np.vstack((B, E)).T
CF = np.vstack((C, F)).T

eq_AD = np.append(norm_vec(AD), -np.matmul(norm_vec(AD), A))
eq_BE = np.append(norm_vec(BE), -np.matmul(norm_vec(BE), B))
eq_CF = np.append(norm_vec(CF), -np.matmul(norm_vec(CF), C))
print(eq_AD)
print(eq_BE)
print(eq_CF) 