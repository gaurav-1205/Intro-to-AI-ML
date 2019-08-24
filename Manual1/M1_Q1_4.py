import numpy as np
import matplotlib.pyplot as plt

def dir_vec(AB):
	return np.matmul(AB, dvec)


def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB, dvec))

A = np.array([-2, -2])
B = np.array([1, 3])

dvec = np.array([-1, 1])

omat = np.array([[0, 1], [-1, 0]])

AB = np.vstack((A, B)).T

print(dir_vec(AB))
print(norm_vec(AB))