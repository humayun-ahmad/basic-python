'''
consider two linear equation:

4*x + 3*y = 20
-5*x + 9*y= 26

There are multiple ways to solve such a system, here I will use matrix solution.
In the matrix solution, the system of linear equations to be solved is
 represented in the form of matrix AX = B. 


A = [[4, 3], [-5, 9]]
X = [[x], [y]]
B = [[20], [26]]

'''

'''
To find the value of x and y variables in Equation 1, we need to find the values
in the matrix X. To do so, we can take the dot product of the inverse of matrix 
A, and the matrix B as shown below

X = inverse(A).B

'''

# import linear matrix equation solving method or function
import numpy as np

m_list =  [[4, 3], [-5, 9]]

A = np.array(m_list)

# for find inverse of A

# inv_A = np.linalg.inv(A)

'''
To find the dot product with the Numpy library, the linalg.dot() function is used.
The following script finds the dot product between the inverse of matrix A and
the matrix B
'''

B = np.array([20,26])
X = np.linalg.inv(A).dot(B)

print(X)


# Using the solve() Method

'''
In the previous two examples, we used linalg.inv() and linalg.dot() methods to
find the solution of system of equations. However, the Numpy library contains
the linalg.solve() method, which can be used to directly find the solution of
a system of linear equations:


Consider the system of equation:
4x + 3y + 2z = 25
-2x + 2y + 3z = -10
3x -5y + 2z = -4

'''

A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
B = np.array([25, -10, -4])
X2 = np.linalg.solve(A,B)

print(X2)
