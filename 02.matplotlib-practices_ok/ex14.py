# 제목, 축, 이름, 눈금, 눈금이름
"""
    1. set_xticklabels() 함수를 사용하면 눈금에 다른 이름을 사용할 수 있다.
    2. set_xticks() 함수와 함께 사용되면 set_xticks() 함수는 무시된다
"""
from matplotlib import pyplot as plt
from numpy.random import randn

fig, sp = plt.subplots(2, 1)
sp[0].plot(randn(1000).cumsum())
sp[1].plot(randn(1000).cumsum())
sp[1].set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
sp[1].set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'], fontsize='small',
                      rotation=30)

plt.show()