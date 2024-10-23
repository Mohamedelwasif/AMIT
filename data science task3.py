import numpy as np

# Initialize a 5x5 matrix with all elements set to 3
matrix = np.full((5, 5), 3)

# Set the first diagonal (1s)
np.fill_diagonal(matrix, 1)

# Set the second diagonal (2s)
np.fill_diagonal(np.fliplr(matrix), 2)

print(matrix)
