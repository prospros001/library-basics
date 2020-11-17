# 1차원 배열 조회
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

for index in range(arr1.size):
    print(f'{index} : {arr1[index]}')