import numpy as np

array = np.random.uniform(0, 10, 20)
rounded_array = np.round(array, 2)
print("Original Array (rounded):")
print(rounded_array)

min_val = np.min(rounded_array)
max_val = np.max(rounded_array)
median_val = np.median(rounded_array)
print("\nMin:", min_val)
print("Max:", max_val)
print("Median:", median_val)

modified_array = np.where(rounded_array < 5, rounded_array**2, rounded_array)
print("\nModified Array (elements < 5 squared):")
print(np.round(modified_array, 2))

def numpy_alternate_sort(array):
    sorted_array = np.sort(array)
    result = []
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        result.append(sorted_array[left])
        if left != right:
            result.append(sorted_array[right])
        left += 1
        right -= 1
    return np.array(result)

alt_sorted_array = numpy_alternate_sort(rounded_array)
print("\nAlternately Sorted Array:")
print(alt_sorted_array)
