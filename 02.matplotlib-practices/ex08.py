# figure & subplot

"""
subplot() 함수 사용
추가옵션 사용해보기
sharex : 서브플롯이 x축 눈금을 같이 쓴다.
sharey : 서브플롯이 y축 눈금을 함께 쓴다.
"""


from matplotlib import pyplot as plt
from numpy.random import randn
import numpy as np

fig, sp = plt.subplots(2, 2, sharex=True, sharey=True)

for i in range(2):
    for j in range(2):
        sp[i, j].hist(randn(100), color='k', alpha=0.3)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0, hspace=0)
plt.show()
