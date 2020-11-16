# 색상, 마커, 선 스타일

'''
 set_xticks() 매서드를 사용하여 x축의 눈금을 변경할수 있다.
'''


from matplotlib import pyplot as plt
from numpy.random import randn

fig, sp = plt.subplots(2, 1)
sp[0].plot(randn(1000).cumsum())
sp[1].plot(randn(1000).cumsum())
sp[1].set_xticks([0, 100, 200, 300, 400])
plt.show()