import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

new_arr = np.array_split(arr, 3)

print([new_arr])