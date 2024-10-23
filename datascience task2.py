# import numpy as np

# Create a 5x5 matrix filled with ones
matrix = np.ones((5, 5), dtype=int)

# Set the inner part to zero
matrix[1:-1, 1:-1] = 0

print(matrix)
