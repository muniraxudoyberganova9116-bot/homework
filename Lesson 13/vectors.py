import numpy as np
print("1. Create a vector with values ranging from 10 to 49.")
v = np.arange(10, 50)
print("vector:\n", v)
print("The length:",len(v))
print(v[0], "and", v[-1], "are the first and last elements")
print("Shape:", v.shape)


print("\n2. Create a 3x3 matrix with values ranging from 0 to 8.")
v2 = np.arange(0, 9).reshape(3,3)
print("V = \n", v2)
print("Shape: ", v2.shape)

print("\n3. Create a 3x3 identity matrix.")
v3 = np.eye(3)
print("Vector : ", v3)

print("\n4. Create a 3x3x3 array with random values.")
v4 = np.random.random((3,3,3))
print("Vector : \n", v4)
print("Shape: ", v4.shape)

print("\n5. Create a 10x10 array with random values and find the minimum and maximum values.")
v5 = np.random.random((10,10))
print("Maximum = ", v5.max())
print("Minimum = ", v5.min())
print("Shape: ", v5.shape)
#print("The vector =\n", v5 )

print("\n6. Create a random vector of size 30 and find the mean value.")
v6 = np.random.random((30))
print('Vector:\n', v6)
print('Mean = ', v6.mean())
print('Shape, ', v6.shape)

print("\n7. Normalize a 5x5 random matrix.")
v7 = np.random.random((5, 5))
normalized = (v7 - v7.min()) / (v7.max() - v7.min())
print('Vector: ', v7)
print('After Normalized \nVector = \n', normalized)

print('Min =', normalized.min())
print('Max = ', normalized.max())

print("\n8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).")
A = np.random.random((5, 3))
B = np.random.random((3, 2))

v8 = A @ B

print("A shape:", A.shape)      
print("B shape:", B.shape)     
print("Result shape:", v8.shape)  # (5, 2)
print(v8)


print("\n9. Create two 3x3 matrices and compute their dot product.")
C = np.random.random((3, 3))
D = np.random.random((3, 3))

v9 = np.dot(C, D)

print("A=\n", A)
print("B=\n", B)
print('Result = \n', v9)
print('Shape =', v9.shape )

print("\n10. Given a 4x4 matrix, find its transpose.")
v10 = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12],
              [13, 14, 15, 16]])

t = v10.T

print("Original:\n", v10)
print("\nTransposed:\n", t)
print("\nOriginal shape:", v10.shape)   # (4, 4)
print("Transposed shape:", t.shape)  # (4, 4)

print("\n11. Create a 3x3 matrix and calculate its determinant.")
v11 = np.random.random((3, 3))
det = np.linalg.det(v11)
print('Matrix:\n', det)
print('\ndet =', det)

print("\n12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \). ") 
A = np.random.random((3, 4))
B = np.random.random((4,3))

result = A @ B

print("A shape:", A.shape)       # (3, 4)
print("B shape:", B.shape)       # (4, 3)
print("Result shape:", result.shape)  # (3, 3)
print("\nResult:\n", result)

print("\n13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  ")
A = np.random.random((3, 3))
a = np.random.random((3, 1))

v13 = A @ a
print("A shape:", A.shape)       # (3, 3)
print("a shape:", a.shape)       # (3, 1)
print("Result shape:", v13.shape)  # (3, 1)
print("\nResult:\n", v13)

print("\n14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector. ")

A = np.array([[2., 1., 1.],
              [1., 3., 2.],
              [1., 1., 4.]])

b = np.array([8., 13., 12.])

x = np.linalg.solve(A, b)

print("Solution:", x)

print("Verification A @ x:", A @ x)  # should equal b
print("Original b:        ", b)

print("\n15. Given a 5x5 matrix, find the row-wise and column-wise sums.")

v15 = np.random.random((5, 5))

print("Matrix:\n", v15)
print("\nRow-wise sum:   ", v15.sum(axis=1)) 
print("Column-wise sum:", v15.sum(axis=0))   
print("Total sum:      ", v15.sum())       