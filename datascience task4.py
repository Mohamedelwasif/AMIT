import numpy as np

# Coefficient matrix (A)
A = np.array([
    [3, 5, 9],
    [2, 4, 8],
    [1, 7, 6]
])

# Variable vector (x)
x = np.array([
    [1],  # Example values for x1
    [1],  # Example values for x2
    [1]   # Example values for x3
])

# Bias vector (b)
b = np.array([
    [10],
    [8],
    [12]
])

# Calculate the result of A * x
result = np.dot(A, x)

print("Matrix A * x:")
print(result)

# Check if the result matches vector b
if np.array_equal(result, b):
    print("The system holds true.")
else:
    print("The system does not match.")
