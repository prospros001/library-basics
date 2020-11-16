# 색상, 마커, 선 스타일

'''
 plot 메서드의 drawStyle 인자를 통해 점의 연결ㄹ을 계단 모양으로 바꿀수 있다.


default, steps, steps-pre, steps-mid , steps-post

'''


from matplotlib import pyplot as plt
from numpy.random import randn

fig, sp = plt.subplots(1, 1)
sp.plot(randn(50).cumsum(), drawStyle='steps-mid',  color='blue', linestyle='solid', marker='')
plt.show()