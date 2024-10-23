# pip install numpy

 # import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array (Matrix):\n", matrix)

# Generate an array of zeros
zeros = np.zeros((2, 3))
print("\nArray of Zeros:\n", zeros)

# Generate an array of random numbers
random_arr = np.random.random((3, 3))
print("\nRandom Array:\n", random_arr)

# Perform mathematical operations
arr_sum = np.sum(arr)
print("\nSum of Array:", arr_sum)

arr_mean = np.mean(arr)
print("Mean of Array:", arr_mean)