import cvxpy as cvp
import numpy as np



x_vec = cvp.Variable((2,1), nonneg=False)

# print(x_vec.shape)

func = (x_vec[0]-8)**2 + (x_vec[1]-6)**2
constraint = [x_vec[0] + x_vec[1] - 18 >=0]

obj = cvp.Minimize(func)

cvp.Problem(obj, constraint).solve()

print(func.value)
print('')
print(x_vec.value)
print(x_vec)