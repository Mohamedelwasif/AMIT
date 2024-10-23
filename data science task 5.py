import numpy as np

# Create two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

# Stack matrices vertically
stacked_matrix = np.vstack((A, B))

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nStacked Matrix:")
print(stacked_matrix)
