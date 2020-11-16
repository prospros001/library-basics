import numpy as np

# 2차원 배열
arr1 = np.array([[1, 2, 3], [10, 20, 20], [100, 200, 300], [1000, 2000, 3000]])
print(arr1, arr1.ndim, arr1.shape)

# 오류 - 길이가 다른 차원 배열

# arr2 = np.array([[1,], [10, 20], [100, 200]])