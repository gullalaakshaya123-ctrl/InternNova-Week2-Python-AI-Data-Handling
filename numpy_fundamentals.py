
# Task 1: NumPy Fundamentals
# InternNova - Week 2

import numpy as np

# 1. Creating NumPy arrays
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

# 2. Creating a 2D array
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])
print("\n2D Array:")
print(arr2)

# 3. Array indexing
print("\nIndexing:")
print("First element:", arr1[0])
print("Second row, third column:", arr2[1, 2])

# 4. Array slicing
print("\nSlicing:")
print("Elements from index 1 to 3:", arr1[1:4])

# 5. Shape and dimensions
print("\nShape and Dimensions:")
print("Shape of 1D array:", arr1.shape)
print("Dimensions of 1D array:", arr1.ndim)
print("Shape of 2D array:", arr2.shape)
print("Dimensions of 2D array:", arr2.ndim)

# 6. Basic mathematical operations
print("\nMathematical Operations:")
print("Addition:", arr1 + 5)
print("Subtraction:", arr1 - 5)
print("Multiplication:", arr1 * 2)
print("Division:", arr1 / 2)

# 7. Statistical operations
print("\nStatistical Operations:")
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Sum:", np.sum(arr1))
