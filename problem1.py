import numpy as np

array = np.random.randint(1, 51, (5, 4))
print("Original Array:")
print(array)

diagonal = [array[i, -1 - i] for i in range(min(array.shape))]
print("\nAnti-diagonal elements (top-right to bottom-left):", diagonal)

max_per_row = np.max(array, axis=1)
print("\nMaximum value in each row:", max_per_row)

mean_val = np.mean(array)
filtered_array = array[array <= mean_val]
print(f"\nMean of the array: {mean_val:.2f}")
print("Elements less than or equal to the mean:", filtered_array)

def numpy_boundary_traversal(matrix):
    rows, cols = matrix.shape
    boundary = []
    boundary.extend(matrix[0, :])
    boundary.extend(matrix[1:rows-1, -1])
    if rows > 1:
        boundary.extend(matrix[-1, ::-1])
    if cols > 1:
        boundary.extend(matrix[rows-2:0:-1, 0])
    return boundary

boundary_elements = numpy_boundary_traversal(array)
print("\nBoundary traversal (clockwise):", boundary_elements)
