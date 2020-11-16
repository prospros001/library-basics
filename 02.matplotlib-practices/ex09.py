# figure & subplot

"""
하나의 서브 플롯에 2개 이상의 그래프를 그리는 것도 가능하다.
2개 이상의 그래프를 구분하기 위해 legend(범례) 룰 사용할수 있따.
"""


from matplotlib import pyplot as plt


fig, sp = plt.subplots(1, 1)

sp.plot([10, 20, 30, 40], label='data1')
sp.plot([9, 15, 21, 27], label='data2')

plt.legend(loc='best')
plt.show()
