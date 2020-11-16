# figure & subplot

"""
크기가 1 X 2 인 figure 2개의 서브 플롯을 추가한 예

"""

from matplotlib import pyplot as plt

fig = plt.figure()
sp1 = fig.add_subplot(2,1,1)
sp2 = fig.add_subplot(2,1,2)

sp1.plot([2, 3, 4, 5], [81, 93, 91, 97])
sp2.plot([2, 3, 4, 5], [81, 93, 91, 97])

plt.show()