import numpy as np
import matplotlib.pyplot as plt

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

def mid_pt(A, B):
	return (A+B)/2.0

dvec = np.array([-1, 1])
omat = np.array([[0, 1], [-1, 0]])

AB = np.vstack((A, B)).T
BC = np.vstack((B, C)).T
CA = np.vstack((C, A)).T

eq_AB = np.append(norm_vec(AB), -np.matmul(norm_vec(AB), A))
eq_BC = np.append(norm_vec(BC), -np.matmul(norm_vec(BC), B))
eq_CA = np.append(norm_vec(CA), -np.matmul(norm_vec(CA), C))
print(eq_AB)

len_AB = np.linalg.norm(A-B)
len_BC = np.linalg.norm(B-C)
len_CA = np.linalg.norm(C-A)

I = (len_BC*A+len_CA*B+len_AB*C)/(len_AB+len_BC+len_CA)

len_IX = (np.linalg.norm(np.matmul(norm_vec(AB), I-A)))/(np.linalg.norm(norm_vec(AB)))
print(len_IX)

#For Circumcircle
#Let O be the circumcentre
#Let X, Y, Z be the perpendicular bisectors
X = mid_pt(B, C)
Y = mid_pt(A, C)
Z = mid_pt(A, B)

eq_OX = line_intersect(dir_vec(BC), BC, np.matmul(dir_vec(BC), X))
eq_OY = line_intersect(dir_vec(CA), CA, np.matmul(dir_vec(CA), Y))
eq_OZ = line_intersect(dir_vec(AB), AB, np.matmul(dir_vec(AB), Z))

len = 10

lam_1 = np.linspace(0, 1, len)

x_AB = np.zeros((2,len))
x_BC = np.zeros((2,len))
x_CA = np.zeros((2,len))

for i in range(len):
	temp1 = A + lam_1[i]*(B-A)
	x_AB[:,i]= temp1.T
	temp2 = B + lam_1[i]*(C-B)
	x_BC[:,i]= temp2.T
	temp3 = C + lam_1[i]*(A-C)
	x_CA[:,i]= temp3.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1), 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1), 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) ,'C')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')

incircle = plt.Circle(I, len_IX, fill=False)
plt.gcf().gca().add_artist(incircle)
plt.grid() # minor


plt.show()