# 배열 차원 전환

import numpy as np


# 사이즈 12인 1차원 배열
arr1 = np.arange(1, 13)
print(arr1)


# 2 X 6 2차원 배열
arr2 = arr1.reshape(2, 6)
print(arr2)

# 2 X 2 X 3 3차원 배열
arr3 = arr1.reshape(2, 2, 3)
print(arr3)