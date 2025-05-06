# Access splitted arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = np.array_split(arr, 3)

print([new_arr[0]])
print([new_arr[1]])
print([new_arr[2]])