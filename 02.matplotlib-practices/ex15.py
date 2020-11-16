# 색상, 마커, 선 스타일

'''
    축의이름 : set_xlabel(), set_ylabel() 함수
    그래프의 이름 : set_title() 함수

    '''


from matplotlib import pyplot as plt
from numpy.random import randn

fig, sp = plt.subplots(2, 1)
sp[0].plot(randn(1000).cumsum())
sp[1].set_xticks([0, 100, 200, 300, 400, 500])
sp[1].set_xticklabels(['pt0', 'pt1', 'pt2', 'pt3', 'pt4'], fontsize='small', rotation=30)

sp.set_xlabel('points')
sp.set_ylabel('counts')

sp.set_title('My First Matplotlib Gragh')
plt.show()