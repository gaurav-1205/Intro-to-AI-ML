import cvxpy as cvp
import numpy as np

x_vec = cvp.Variable((2,1), nonneg=False)

# print(x_vec.shape)

func = 4*(x_vec[0])**2 + 2*(x_vec[1])**2
constraint = [3*x_vec[0] + x_vec[1] - 8 == 0, 15 - 2*x_vec[0] - 4*x_vec[1] >= 0]

obj = cvp.Minimize(func)

cvp.Problem(obj, constraint).solve()

print(func.value)
print(x_vec.value)
print(x_vec)