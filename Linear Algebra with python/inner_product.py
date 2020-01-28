u,v = [2,-5,-1],[4,2,-3]

#####################
inner_prod = 0

for i in range(len(u)):
	inner_prod += u[i]*v[i]

#print(inner_prod)

#######################
# using numpy library
import numpy as np

u = np.array(u)
v = np.array(v)

inner_prod1 = np.inner(u,v)
# print(inner_prod1)

######################
#for 1-D array np.inner(u,v) is same as sum(u[:] * v[:])
inner_prod2 = sum(u[:]*v[:])
# print(inner_prod2)

#####################
x = np.array([[1], [2]])
x_trans = np.transpose(x)
out = np.dot(x_trans,x)
print(out)




